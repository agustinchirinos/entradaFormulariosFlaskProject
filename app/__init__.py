from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)


db = SQLAlchemy()
migrate = Migrate()

engine = create_engine("postgresql://postgres:123456@localhost:5432/tutorialFlask")

from .xssreflejado import xssreflejado
from .xssalmacenado import xssalmacenado
from .sqlinjection import sqlinjection


def create_app():
    app.secret_key = "ClaveSecreta"
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@localhost:5432/tutorialFlaskORM"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # db.init_app(app)
    #
    # migrate.init_app(app, db)


    app.register_blueprint(xssreflejado)
    app.register_blueprint(xssalmacenado)
    app.register_blueprint(sqlinjection)
    return app