import os
import click
from app import create_app
from app.models import db, User
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

print(os.environ['APP_SETTINGS'])
app = create_app(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    """ Creates a python REPL with several default imports
        in the context of the app
    """
    return dict(app=app, db=db, User=User)
