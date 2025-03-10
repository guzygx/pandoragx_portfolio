import os
from flask import Flask, render_template, send_from_directory,  g, request
from flask_babel import Babel, _
from .blueprints.bundle import bundle

LANGUAGES = {
    'en': 'English',
    'fr': 'Français'
}

def get_locale():
    language = g.get('lang_code')
    return language if language in LANGUAGES else 'en'

app = Flask(__name__, template_folder=".")
app.register_blueprint(bundle)
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './i18n'

babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico')

@app.route('/app/static/dist/bundled/<bundle>')
def serve_bundle(bundle):
    return send_from_directory(
        os.path.join(app.root_path, 'static/dist/bundled'), bundle)    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('layouts/404.html'), 404

@app.route('/<lang>')
def index(lang):
    if lang not in LANGUAGES:
        # return 'Invalid language', 404
        return page_not_found("invalid language")
        
    # Set the language for this request
    g.lang_code = lang
    
    print("lang:", lang)
    greeting = _('hello')
    
    return render_template('pages/index.html', greeting=greeting)

# @app.route("/")
# def index():
#     return render_template('pages/index.html')

@app.route("/contact")
def contact():
    return render_template('pages/contact.html')

@app.route("/about")
def about():
    return render_template('pages/about.html')

@app.route("/works/<project>")
def describe(project):
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')