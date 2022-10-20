from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
# from .config import settings

# "pool_pre_ping": True to set to pessimistic disconnect handling was suggested, but apparently unnecessary
db = SQLAlchemy(engine_options={"pool_recycle": 280})
migrate = Migrate()

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
