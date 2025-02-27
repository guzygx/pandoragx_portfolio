import os
from flask import Flask, render_template, send_from_directory
from .blueprints.bundle import bundle_blueprint

app = Flask(__name__, template_folder=".")
app.register_blueprint(bundle_blueprint)

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

@app.route("/")
def index():
    return render_template('pages/index.html')

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