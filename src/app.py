import os
from flask import Flask, render_template, send_from_directory
from helpers.config.assets_blueprint import assets_blueprint

def create_app(test_config=None):
    app = Flask(
        __name__,
        static_url_path="/",
        static_folder="static",
        template_folder=".",
    )
    app.register_blueprint(assets_blueprint)
    
    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(
            os.path.join(app.root_path, 'static'),
            'favicon.ico', 
            mimetype='image/vnd.microsoft.icon')
        
    @app.route('/dist/bundled/<asset>')
    def serve_assets(asset):
        return send_from_directory(
            os.path.join(app.root_path, '../dist/bundled'), asset)    
    
    @app.errorhandler(404)
    def page_not_found(e):
        # note that we set the 404 status explicitly
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

    return app
