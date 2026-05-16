from flask import Flask
from .config import Config, db_connection
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#untuk inisialisasi 
bcrypt = Bcrypt()
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    #untuk memanggil config
    app.config.from_object(Config)
    #untuk tes koneksi database
    db_connection()

    # untuk inisialisasi database, migrasi, dan bcrypt
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    #daftar models
    from app.models import user

    #untuk memanggil route
    from app.routes.base_routes import base
    app.register_blueprint(base, url_prefix="/")
    return app