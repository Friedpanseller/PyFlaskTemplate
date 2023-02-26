import flask, flask_login, flask_cors, flask_session, werkzeug, sqlalchemy, flask_sqlalchemy
from app.models import *

db = flask_sqlalchemy.SQLAlchemy()

app = flask.Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)

with app.app_context():
    db.create_all()

cors = flask_cors.CORS(app, supports_credentials=True)

from app.routes import mod_api as api_module

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong" 

@login_manager.user_loader
def user_loader(user_id):
    return User.query.filter(User.id == user_id).first()
    
@app.errorhandler(werkzeug.exceptions.HTTPException)
def http_error(error):
    try:
        return error.name, error.code
    except:
        return error, 500

@app.route("/")
def home():
    return "Success"
