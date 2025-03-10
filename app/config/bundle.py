import json
import os
from pathlib import Path
from flask import Blueprint, send_from_directory, current_app

FLASK_DEBUG = os.getenv("FLASK_DEBUG", "0")
VITE_ORIGIN = os.getenv("VITE_ORIGIN", "http://localhost:5173")

is_production = FLASK_DEBUG != "1"
project_path = Path(os.path.dirname(os.path.abspath(__file__)))

bundle = Blueprint("bundle_blueprint", __name__)

manifest = {}
if is_production:
    manifest_path = "app/static/dist/manifest.json"
    with open(manifest_path, "r") as content:
        manifest = json.load(content)

@bundle.app_context_processor
def add_context():
    def dev_bundle(file_path):
        return f"{VITE_ORIGIN}/{file_path}"

    def prod_bundle(file_path):
        try:
            return f"app/static/dist/{manifest[file_path]['file']}"
        except:
            return "bundle-blueprint-error"

    return {
        "bundle": prod_bundle if is_production else dev_bundle,
        "is_production": is_production,
    }

@bundle.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(current_app.root_path, 'static'),
        'favicon.ico')

@bundle.route('/app/static/dist/bundled/<bundle>')
def serve_bundle(bundle):
    return send_from_directory(
        os.path.join(current_app.root_path, 'static/dist/bundled'), bundle)    