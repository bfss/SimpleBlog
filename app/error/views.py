from flask import render_template

from . import error

@error.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@error.app_errorhandler(500)
def intel_error(error):
    return render_template('500.html'), 404