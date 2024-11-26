from app import db, User

# Initialize database
db.create_all()

# Add sample users
doctor = User(username='DrSmith', password='pass123', role='doctor')
patient = User(username='JohnDoe', password='pass123', role='patient')

db.session.add(doctor)
db.session.add(patient)
db.session.commit()

print("Database setup complete with sample users!")
