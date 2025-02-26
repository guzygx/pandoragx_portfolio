import json
import os
from pathlib import Path
from flask import Blueprint

FLASK_DEBUG = os.getenv("FLASK_DEBUG", "0")
VITE_ORIGIN = os.getenv("VITE_ORIGIN", "http://localhost:5173")

is_production = FLASK_DEBUG != "1"
project_path = Path(os.path.dirname(os.path.abspath(__file__)))

assets_blueprint = Blueprint(
    "assets_blueprint",
    __name__,
    static_folder="./src/static",
    static_url_path="/src/static",
)

manifest = {}
if is_production:
    manifest_path = "dist/manifest.json"
    with open(manifest_path, "r") as content:
        manifest = json.load(content)

@assets_blueprint.app_context_processor
def add_context():
    def dev_asset(file_path):
        return f"{VITE_ORIGIN}/{file_path}"

    def prod_asset(file_path):
        try:
            return f"dist/{manifest[file_path]['file']}"
        except:
            return "asset-not-found"

    return {
        "asset": prod_asset if is_production else dev_asset,
        "is_production": is_production,
    }