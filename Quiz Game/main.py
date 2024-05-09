import requests
from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quiz', methods=['POST'])
def start_quiz():
    category = request.form.get('category')
    difficulty = request.form.get('difficulty')

    api_link = f"https://opentdb.com/api.php?amount=10&category={category}&difficulty={difficulty}&type=multiple"

    response = requests.get(api_link)
    quiz_data = response.json()

    questions = []
    for result in quiz_data['results']:
        question = result['question']
        correct_answer = result['correct_answer']
        incorrect_answers = result['incorrect_answers']
        options = [correct_answer] + incorrect_answers
        random.shuffle(options)
        questions.append({'question': question, 'options': options, 'correct_answer': correct_answer})

    # Extract category name from the JSON data
    category_name = quiz_data['results'][0]['category']

    # Pass category name to the template
    return render_template('quiz.html', questions=questions, category_name=category_name)


@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    score = 0
    total_questions = len([q for q in request.form if q.endswith('_correct')])
    for question in request.form:
        user_answer = request.form[question]
        correct_answer = request.form.get(f"{question}_correct")
        if user_answer == correct_answer:
            score += 1

    return render_template('score.html', score=score, total_questions=total_questions)


if __name__ == '__main__':
    app.run(debug=True)
