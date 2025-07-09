from app import app, db
from models import User
from werkzeug.security import generate_password_hash

with app.app_context():
    # Check if admin already exists
    admin = User.query.filter_by(email="admin@example.com").first()
    if not admin:
        admin = User(
            username="admin",
            email="admin@example.com",
            password=generate_password_hash("admin123"),  # change if needed
            role="admin"
        )
        db.session.add(admin)
        db.session.commit()
        print("✅ Admin user created successfully.")
    else:
        print("⚠️ Admin already exists.")
