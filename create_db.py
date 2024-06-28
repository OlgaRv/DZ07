from flask_auth_app import db, app
from flask_auth_app.models import User

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.commit()