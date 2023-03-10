# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database
SESSION_TYPE = "sqlalchemy"
SESSION_SQLALCHEMY_TABLE = "__sessions"

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

PYTHONUNBUFFERED = True

# Application threads. A common general assumption is
# using 2 per available processor cores to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "PLEASE_SET_A_KEY_HERE"

# Secret key for signing cookies
SECRET_KEY = "PLEASE_SET_A_KEY_HERE"
