from flask import Flask
from .config import db_connection

def create_app():
    app = Flask(__name__)

    #untuk memanggil config
    app.config.from_object(config)
    #untuk tes koneksi database
    db_connection()
    #untuk memanggil route
    from .routes.base_routes import base
    app.register_blueprint(base, url_prefix="/")
    return app