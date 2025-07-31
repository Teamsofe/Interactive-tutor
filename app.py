from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import *

app = Flask(__name__)

# Configuring the SQLite database
app.config['SECRET_KEY'] = 'faith_project'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        reg_no = request.form['reg_no']
        email = request.form['email']
        password = request.form['password']

        # Check if the student exists in the database
        student = Student.query.filter_by(reg_no=reg_no, email=email).first()

        if student and student.password == password:
            session['student_reg_no'] = student.reg_no
            flash(f"Welcome, {student.name}! You are successfully logged in.", 'success')
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials. Please try again.", 'danger')

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    # Assuming the student is logged in and their reg_no is stored in session
    student_reg_no = session.get('student_reg_no')

    if student_reg_no:
        student = Student.query.filter_by(reg_no=student_reg_no).first()
        topics = Topic.query.all()
        quiz_results = QuizResult.query.filter_by(student_reg_no=student_reg_no).all()

        return render_template('dashboard.html', student=student, topics=topics, quiz_results=quiz_results)

    return redirect(url_for('login'))  # Redirect if student is not logged in


@app.route('/topics')
def topics():
    student_reg_no = session.get('student_reg_no')
    if student_reg_no:
        topics = Topic.query.all()
        return render_template('topics.html', topics=topics)
    return redirect(url_for('login'))


@app.route('/bubble_sort_quiz', methods=['GET', 'POST'])
def bubble_sort_quiz():
    score = None
    if request.method == 'POST':
        # Fetch answers safely
        q1 = request.form.get('q1')
        q2 = request.form.get('q2')
        q3 = request.form.get('q3')
        q4 = request.form.get('q4')
        q5 = request.form.get('q5')

        correct_answers = {
            'q1': 'b',
            'q2': 'a',
            'q3': 'a',
            'q4': 'b',
            'q5': 'b'
        }
        score = sum([
            q1 == correct_answers['q1'],
            q2 == correct_answers['q2'],
            q3 == correct_answers['q3'],
            q4 == correct_answers['q4'],
            q5 == correct_answers['q5']
        ])
    return render_template('bubble_sort_quiz.html', score=score)


@app.route('/bubble-sort', methods=['GET', 'POST'])
def bubble_sort():
    simulation_result = None
    if request.method == 'POST':
        try:
            numbers = list(map(int, request.form['numbers'].split(',')))
            steps = []
            arr = numbers[:]
            n = len(arr)
            for i in range(n):
                for j in range(n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    steps.append(f"Pass {i+1}, Step {j+1}: {arr}")
            simulation_result = steps
        except:
            simulation_result = ["Invalid input. Please enter numbers only."]
    return render_template('bubble_sort.html', simulation_result=simulation_result)


@app.route('/insertion_sort', methods=['GET', 'POST'])
def insertion_sort():
    simulation_result = []
    numbers_input = ''

    if request.method == 'POST':
        numbers_input = request.form['numbers']
        try:
            array = list(map(int, numbers_input.strip().split(',')))
            original = array[:]

            simulation_result.append(f"Original list: {original}")
            for i in range(1, len(array)):
                key = array[i]
                j = i - 1
                simulation_result.append(f"🔍 Considering {key} at position {i}")
                while j >= 0 and array[j] > key:
                    simulation_result.append(f"🔁 Swapping {array[j]} and {array[j + 1]}")
                    array[j + 1] = array[j]
                    j -= 1
                    simulation_result.append(f"Current list: {array}")
                array[j + 1] = key
                simulation_result.append(f"✅ Inserted {key} at position {j + 1}")
                simulation_result.append(f"After iteration {i}: {array}")
            simulation_result.append(f"✅ Final sorted list: {array}")

        except ValueError:
            simulation_result.append("❌ Error: Please enter a list of numbers separated by commas.")

    return render_template('insertion_sort.html', simulation_result=simulation_result, numbers_input=numbers_input)



@app.route('/insertion_sort_quiz', methods=['GET', 'POST'])
def insertion_sort_quiz():
    score = None

    if request.method == 'POST':
        # Getting the answers from the quiz
        answers = {
            'q1': request.form.get('q1'),
            'q2': request.form.get('q2'),
            'q3': request.form.get('q3'),
            'q4': request.form.get('q4'),
            'q5': request.form.get('q5')
        }

        # Correct answers
        correct_answers = {
            'q1': 'b',
            'q2': 'a',
            'q3': 'a',
            'q4': 'b',
            'q5': 'b'
        }

        # Check answers
        score = sum([1 for key in answers if answers[key] == correct_answers[key]])

        # Flash message for result
        flash(f'Your Score: {score} out of 5', 'success')

    return render_template('insertion_sort_quiz.html', score=score)  # The result will appear in the same page

@app.route('/linear_search', methods=['GET', 'POST'])
def linear_search():
    simulation_result = None
    if request.method == 'POST':
        numbers = request.form['numbers'].split(',')
        numbers = [int(num.strip()) for num in numbers]
        target = int(request.form['target'])

        # Linear Sarch Simulation
        steps = []
        for i, num in enumerate(numbers):
            steps.append(f"Checking index {i}: {num}")
            if num == target:
                steps.append(f"Target {target} found at index {i}")
                break
        else:
            steps.append(f"Target {target} not found in the list")

        simulation_result = steps

    return render_template('linear_search.html', simulation_result=simulation_result)


@app.route('/linear_search_quiz', methods=['GET', 'POST'])
def linear_search_quiz():
    score = None

    if request.method == 'POST':
        # Match the HTML names: question1, question2, question3
        answers = {
            'question1': request.form.get('question1'),
            'question2': request.form.get('question2'),
            'question3': request.form.get('question3')
        }

        # Correct answers
        correct_answers = {
            'question1': 'a',
            'question2': 'c',
            'question3': 'b'
        }

        # Calculate score
        score = sum([1 for key in answers if answers[key] == correct_answers[key]])

    return render_template('linear_search_quiz.html', score=score)

@app.route('/binary_search', methods=['GET', 'POST'])
def binary_search():
    simulation_result = None

    if request.method == 'POST':
        if 'numbers' in request.form and 'target' in request.form:
            # Handling Simulation
            numbers = request.form['numbers'].split(',')
            numbers = [int(num.strip()) for num in numbers]
            target = int(request.form['target'])

            # Binary Search Simulation
            low, high = 0, len(numbers) - 1
            steps = []
            while low <= high:
                mid = (low + high) // 2
                steps.append(f"Checking middle index {mid}: {numbers[mid]}")
                if numbers[mid] == target:
                    steps.append(f"Target {target} found at index {mid}")
                    break
                elif numbers[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                steps.append(f"Target {target} not found in the list.")
            simulation_result = steps

    return render_template(
        'binary_search.html',
        simulation_result=simulation_result
    )

@app.route('/binary_search_quiz', methods=['GET', 'POST'])
def binary_search_quiz():
    score = None
    if request.method == 'POST':
        answers = {
            'question1': request.form.get('question1'),
            'question2': request.form.get('question2'),
            'question3': request.form.get('question3')
        }

        correct_answers = {
            'question1': 'c',
            'question2': 'b',
            'question3': 'b'
        }

        score = sum(1 for key in correct_answers if answers.get(key) == correct_answers[key])

    return render_template('binary_search_quiz.html', score=score)


@app.route('/recursion', methods=['GET', 'POST'])
def recursion():
    result = None
    number = None

    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            result = factorial(number)
        except (ValueError, KeyError):
            result = "Invalid input. Please enter a valid number."

    return render_template('recursion.html', result=result, number=number)

def factorial(n):
    if n < 0:
        return "Undefined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


@app.route('/recursion_quiz', methods=['GET', 'POST'])
def recursion_quiz():
    score = None
    if request.method == 'POST':
        answers = {
            'question1': 'b',
            'question2': 'b',
            'question3': 'b',
            'question4': 'a',
            'question5': 'a'
        }

        score = 0
        for key, correct in answers.items():
            if request.form.get(key) == correct:
                score += 1

    return render_template('recursion_quiz.html', score=score)


@app.route('/logout')
def logout():
    session.pop('student_reg_no', None)  # Remove the student from session
    return redirect(url_for('login'))  # Redirect to the login page

if __name__ == '__main__':
    app.run(debug=True)
