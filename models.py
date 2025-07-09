from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

# 🧑 User Table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='customer')  # 'admin', 'mechanic', 'customer'

    # Relationships
    bookings = db.relationship('ServiceBooking', backref='user', lazy=True)
    cart_items = db.relationship('Cart', backref='user', lazy=True)
    wishlist_items = db.relationship('Wishlist', backref='user', lazy=True)


# 🔧 Spare Part Table
class SparePart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)  # Optional image

    # Relationships
    cart_items = db.relationship('Cart', backref='part', lazy=True)
    wishlist_items = db.relationship('Wishlist', backref='part', lazy=True)


# 🛠️ Service Booking Table
class ServiceBooking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bike_model = db.Column(db.String(100), nullable=False)
    service_type = db.Column(db.String(100), nullable=False)
    booking_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), default='Pending')  # Pending / In Progress / Completed
    mechanic_note = db.Column(db.Text, nullable=True)


# 🛒 Cart Table
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    part_id = db.Column(db.Integer, db.ForeignKey('spare_part.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)


# ❤️ Wishlist Table
class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    part_id = db.Column(db.Integer, db.ForeignKey('spare_part.id'), nullable=False)
