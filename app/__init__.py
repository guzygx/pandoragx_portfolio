from flask import Flask, abort, g
from flask_babel import Babel
from .config import bundle, errors, get_locale
from .routes import routes

app = Flask(__name__, template_folder="views")

app.config['BABEL_TRANSLATION_DIRECTORIES'] = './locales'
app.config['LANGUAGES'] = {
  'en': 'English',
  'fr': 'French'
}

babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)

app.register_blueprint(bundle)
app.register_blueprint(errors)
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(host='0.0.0.0')