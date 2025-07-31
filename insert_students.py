from models import db, Student
from app import app  # make sure this points to your Flask app object

# Ensure we are working inside the app context
with app.app_context():
    # Optional: Create all tables (if not yet created)
    db.create_all()

    # Create new students
    students = [
        Student(reg_no='2021/123456', name='Precious Udeh', email='john.doe@example.com', password='preciousudeh'),
        Student(reg_no='2022/678912', name='Jane Okafor', email='jane.smith@example.com', password='janeokafor'),
        Student(reg_no='2020/123456', name='Faith Udechukwu', email='faith.udechukwu@gmail.com', password='faithudechukwu'),
        Student(reg_no='2024/678912', name='Blessing Uzo', email='blessing.uzo@yahoo.com', password='blessinguzo')
    ]

# Add to database
    db.session.bulk_save_objects(students)
    db.session.commit()

    print("Students inserted successfully.")
