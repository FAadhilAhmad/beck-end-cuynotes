import uuid
from app import db, bcrypt
from datetime import datetime

class User(db.Model):
    #nama table
    __tablename__ = "users"
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(50), nullable=False)
    profile_img = db.Column(db.String(255))
    thumbnail_img = db.Column(db.String(255))
    created_ad = db.Column(db.DateTime, default=datetime.utcnow)
    updated_ad = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    def set_password(self, password):
        self.password_hash= bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)    