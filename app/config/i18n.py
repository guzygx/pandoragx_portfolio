from flask import g, abort, current_app

def get_locale():
    language = g.get('lang_code')
    return language if language in current_app.config['LANGUAGES']  else abort(404)
