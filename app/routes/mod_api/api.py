import flask
from app.routes.mod_api import mod_api
from app.routes.routes import login_required

@mod_api.route("/", methods=["POST", "GET"])
def api_home():
    return "Success"

@mod_api.route("/secure", methods=["POST", "GET"])
@login_required
def api_secure():
    return "You are logged in :)"
