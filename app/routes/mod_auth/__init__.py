import flask

module_name = "auth"
mod_auth = flask.Blueprint(module_name, __name__, url_prefix="/"+module_name)

from .auth import *