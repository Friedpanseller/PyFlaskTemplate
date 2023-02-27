import flask, flask_cors, flask_session, werkzeug, sqlalchemy, sqlalchemy.orm
from sqlalchemy import create_engine, select
from app.models import Base, User, Session
from app.routes.routes import hash_password

app = flask.Flask(__name__)
app.config.from_pyfile('config.py')
flask_session.Session(app)

engine = create_engine(app.config.get("SQLALCHEMY_DATABASE_URI"))
Base.metadata.create_all(engine)

with sqlalchemy.orm.Session(engine) as session:
    stmt = select(User)
    user = session.execute(stmt).scalar_one_or_none()

    if not user:
        print("No users in database... adding default user")
        user = User(username="leo", hpassword=hash_password("leo", "123"))
        session.add(user)
        session.commit()

cors = flask_cors.CORS(app, supports_credentials=True)

from app.routes.mod_api import mod_api as api_module
app.register_blueprint(api_module)
from app.routes.mod_auth import mod_auth as auth_module
app.register_blueprint(auth_module)
    
@app.errorhandler(werkzeug.exceptions.HTTPException)
def http_error(error):
    try:
        return error.name, error.code
    except:
        return error, 500

@app.route("/")
def home():
    return "Success"
