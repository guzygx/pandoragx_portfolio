from flask import Blueprint, render_template, g
from flask_babel import _

routes = Blueprint("routes", __name__, url_prefix='/<lang_code>')

@routes.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)

@routes.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang_code = values.pop('lang_code')

@routes.route('/')
def index():
    greeting = _('hello')
    return render_template('pages/index.html', greeting=greeting)
  
@routes.route("/contact")
def contact():
    return render_template('pages/contact.html')

@routes.route("/about")
def about():
    return render_template('pages/about.html')

@routes.route("/works/<project>")
def describe(project):
    return "<p>Hello, World!</p>"