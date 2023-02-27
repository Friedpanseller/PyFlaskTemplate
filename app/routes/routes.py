from flask import session
from functools import wraps
import json, hashlib

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session.get("user"):
            return f(*args, **kwargs)
        else:
            return "Not logged in", 401
    return wrap

def unauthorized(auth):
    user = session.get("user")
    if not user or not user.get("auth_value") or user.get("auth_value") > auth.value:
        return True
    return False

def rest_response(status: bool, data=None):
    if data is None:
        data = status

    status = "success" if status else "error"
    
    return json.dumps({
        "status": status,
        "data": data
    }, indent=2, sort_keys=True)

def hash_password(username: str, password: str):
    salt = "!!!CHANGE THIS!!! some lengthy once-upon-a-time story about a lovely couple or something"

    h = hashlib.blake2b()
    h.update(f"{salt}{username}{password}{salt}".encode("utf-32"))

    return h.hexdigest()