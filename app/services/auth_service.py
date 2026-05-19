from app.models.user import User
from app import db

def register_user(input_username, input_email, input_password):
    try:
        # buat cek user dan email 
        if User.query.filter((User.username == input_username) | (User.email == input_email)).first():
            return None, "Username or email already exists"

        # created user baru
        new_user = User(username=input_username, email=input_email)
        new_user.set_password(input_password)
        db.session.add(new_user)
        db.session.commit()
        return new_user, "Register successful"
    
    except Exception as e:
        db.session.rollback()
        return None, f"Failed to register: {e}"