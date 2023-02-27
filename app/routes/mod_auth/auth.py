import flask
from flask import request, render_template
from app.routes.mod_auth import mod_auth
from app.routes.routes import rest_response, hash_password
from app import engine
from app.models import User
from sqlalchemy import select
from sqlalchemy.orm import Session

@mod_auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.jinja2")
    elif request.method == "POST":
        data = request.json
        print(data)

        if not (username := data.get("username")):
            return rest_response(False, "Incorrect username or password")
        
        if not (password := data.get("password")):
            return rest_response(False, "Incorrect username or password")
        
        hpassword = hash_password(username, password)
        print("Username", username)
        print("HPassword", hpassword)
        
        user = None
        with Session(engine) as session:
            stmt = select(User).filter_by(username=username, hpassword=hpassword)
            user = session.execute(stmt).scalar_one_or_none()

        if not user:
            return rest_response(False, "Incorrect username or password")

        flask.session.permanent = True
        flask.session["user"] = user.dict()
        return rest_response(True, user.dict())

@mod_auth.route("/logout", methods=["GET", "POST"])
def logout():
    flask.session["user"] = None
    return "Logged out"