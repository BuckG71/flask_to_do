from app import app, db

print("Starting script...")

def create_database():
    with app.app_context():
        print("Inside app context...")
        db.create_all()
        print("Database tables created successfully.")

if __name__ == "__main__":
    create_database()