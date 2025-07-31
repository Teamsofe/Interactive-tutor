from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

# Student model (formerly User)
class Student(db.Model):
    __tablename__ = 'students'

    reg_no = db.Column(db.String(15), primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Student {self.reg_no}>"

# Topic model (algorithm topics)
class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    video_url = db.Column(db.String(300))
    audio_url = db.Column(db.String(300))

# Quiz model
class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    question = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(200), nullable=False)
    option_b = db.Column(db.String(200), nullable=False)
    option_c = db.Column(db.String(200), nullable=False)
    option_d = db.Column(db.String(200), nullable=False)
    correct_answer = db.Column(db.String(1), nullable=False)  # A, B, C, or D

    topic = db.relationship('Topic', backref=db.backref('quizzes', lazy=True))

# Quiz attempt/result model
class QuizResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_reg_no = db.Column(db.String(15), db.ForeignKey('students.reg_no'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    selected_answer = db.Column(db.String(1))
    is_correct = db.Column(db.Boolean)

    student = db.relationship('Student', backref=db.backref('results', lazy=True))
    quiz = db.relationship('Quiz', backref=db.backref('results', lazy=True))
