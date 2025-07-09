from app import app, db
from models import User
from werkzeug.security import generate_password_hash

with app.app_context():
    admin = User.query.filter_by(email="admin@example.com").first()
    if not admin:
        admin = User(
            username="admin",
            email="admin@example.com",
            password=generate_password_hash("admin123"),
            role="admin"
        )
        db.session.add(admin)

    user = User.query.filter_by(email="user@example.com").first()
    if not user:
        user = User(
            username="user",
            email="user@example.com",
            password=generate_password_hash("user123"),
            role="customer"
        )
        db.session.add(user)

    db.session.commit()
    print("✅ Admin and User created successfully.")
