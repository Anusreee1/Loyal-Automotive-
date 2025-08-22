Loyal Automotive :

Loyal Automotive is a Flask-based web application for managing bike and car services.
It includes features like:

User authentication (Register/Login/Logout)

Spare parts management (CRUD, search, stock)

Wishlist & Cart system

Orders & Booking history

Service booking and management

Role-based access (Admin, Mechanic, Customer)

Notifications & Reports

This project is designed as a mini project / portfolio project for learning and showcasing Flask, SQLite, and Web Development skills.

Tech Stack

Backend: Python (Flask)

Database: SQLite (SQLAlchemy ORM)

Frontend: HTML, CSS, Bootstrap

Authentication: Flask-Login

Other Tools: Jinja2 Templates, WTForms

Project Structure
loyal-automotive/
├── app.py                # Main Flask application
├── requirements.txt      # Project dependencies
├── instance/
│   └── loyalauto.db      # SQLite database (auto-created)
├── static/
│   ├── css/
│   └── images/
├── templates/            # HTML files
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── spare_parts.html
│   └── ...
└── README.md

Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/loyal-automotive.git
cd loyal-automotive

2️⃣ Create & activate virtual environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
python app.py


Now open your browser and go to http://127.0.0.1:5000/

User Roles

Admin – Manage users, bookings, and spare parts.

Mechanic – View & update assigned service requests.

Customer – Browse spare parts, add to cart/wishlist, and book services.

Screenshots (Optional)

Add some screenshots of your app UI here (login page, dashboard, spare parts, etc.)

.gitignore

To avoid pushing unwanted files, create a .gitignore:

venv/
__pycache__/
*.db
*.sqlite3
instance/
*.pyc
.env

License

This project is licensed under the MIT License – feel free to use and modify it.

Contribution

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

Author

Anusree P
📧 Contact: [your-email@example.com
]
🔗 GitHub: [your-github-link]
