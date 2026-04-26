from flask import Flask
from .config import  db_connection
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


bcrypt = Bcrypt()
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    #untuk memanggil config
    app.config.from_object(config)
    #untuk tes koneksi database
    db_connection()
    #untuk memanggil route
    from .routes.base_routes import base
    app.register_blueprint(base, url_prefix="/")
    return app