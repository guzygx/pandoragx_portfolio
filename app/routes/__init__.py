from flask import Blueprint, render_template

routes = Blueprint("routes", __name__)

@routes.route("/contact")
def contact():
    return render_template('pages/contact.html')

@routes.route("/about")
def about():
    return render_template('pages/about.html')

@routes.route("/works/<project>")
def describe(project):
    return "<p>Hello, World!</p>"