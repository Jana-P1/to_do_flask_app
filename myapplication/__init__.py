
from flask import Flask, render_template
import os
from . import db
from myapplication.db import db_session, init_db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('APP_SECRET'),
        DATABASE=os.path.join(app.instance_path, 'myapplication.sqlite'),
    )
    # Removes database sessions at the end of a request or when the application shuts down
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()
    
    init_db()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    
    
    # -------------- BLUEPRINTS ------------------
    from myapplication.users.views import users
    app.register_blueprint(users)

    from myapplication.landing.views import landing
    app.register_blueprint(landing)
   
    return app

