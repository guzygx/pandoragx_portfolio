from flask import Flask, render_template, g, abort
from flask_babel import Babel, _
from .config import bundle, errors, LANGUAGES
from .routes import routes

def get_locale():
    language = g.get('lang_code')
    return language if language in LANGUAGES else 'en'

app = Flask(__name__, template_folder="views")
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './locales'

babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)

app.register_blueprint(bundle)
app.register_blueprint(errors)
app.register_blueprint(routes)


@app.route('/<lang>')
def index(lang):
    if lang not in LANGUAGES:
        abort(404)

    g.lang_code = lang
    greeting = _('hello')
    
    return render_template('pages/index.html', greeting=greeting)

if __name__ == "__main__":
    app.run(host='0.0.0.0')