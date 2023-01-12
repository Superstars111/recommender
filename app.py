from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import settings

# "pool_pre_ping": True to set to pessimistic disconnect handling was suggested, but apparently unnecessary
db = SQLAlchemy(engine_options={"pool_recycle": 280})
migrate = Migrate()

app = Flask(__name__)

app.config.from_object(settings)

db.init_app(app)
migrate.init_app(app, db)

login_manager = LoginManager()
login_manager.login_view = "auth.login"  # Probably needs the auth blueprint to do... whatever it's supposed to do.
login_manager.init_app(app)

from models import User  # Needed lower than top to prevent circular import. There might be a better way to do this.


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Blueprints
from .auth.auth import AUTH_BLUEPRINT as AUTH_BLUEPRINT
app.register_blueprint(AUTH_BLUEPRINT)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
