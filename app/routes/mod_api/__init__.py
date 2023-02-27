import flask

module_name = "api"
mod_api = flask.Blueprint(module_name, __name__, url_prefix="/"+module_name)

from .api import *