from flask import Flask
from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine



app = Flask(__name__)
app.secret_key = "ClaveSecreta"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@localhost:5432/tutorialFlaskORM"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

engine = create_engine("postgresql://postgres:123456@localhost:5432/tutorialFlask")

from .xssreflejado import xssreflejado
from .xssalmacenado import xssalmacenado
from .sqlinjection import sqlinjection
from .file import file
from .contramedidas import contramedidas


def create_app():

    # db.init_app(app)
    app.register_blueprint(xssreflejado)
    app.register_blueprint(xssalmacenado)
    app.register_blueprint(sqlinjection)
    app.register_blueprint(file)
    app.register_blueprint(contramedidas)
    return app