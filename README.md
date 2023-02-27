# Setup
- Edit `run.py` and change `app_name` variable
- Edit `templates/base.jinja2` and change title
- Create favicons and set the right paths in `templates/base.jinja2`
- Edit `config.py` set `SQLALCHEMY_DATABASE_URI` to the type of database you are using
- Edit `config.py` set a complex `CSRF_SESSION_KEY` and `SECRET_KEY`
- Edit `routes/routes.py` set a complex `salt`

## Database Models
- `session.py`: You shouldn't need to edit this, it just stores the sessinos for Flask in the database
- `user.py`: This is the user object the user logs in as. You can add more columns to this if you would like

## Routes
- `mod_api/api.py`: Here you can put all your api routes. The `@login_required` decorator requires users to log in.

## Test
- You can visit `/auth/login` to test logging in, then visit `/api/` to view an unsecured page, or `/api/secured` to view a page you should only be able to access after logging in