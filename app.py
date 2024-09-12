from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# 문장 목록
texts = [
    "가나다라마바사.",
    "사랑하는 나에게.",
    "개발자가 될수 있는지 궁금합니다.",
    "나는 말 하는 감자다.",
    "모든 계절이 유서엿다."
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_text', methods=['GET'])
def get_text():
    selected_text = random.choice(texts)
    return jsonify({'text': selected_text})

@app.route('/check_text', methods=['POST'])
def check_text():
    original_text = request.form['original']
    user_text = request.form['user']
    accuracy = calculate_accuracy(original_text, user_text)
    return jsonify({'accuracy': accuracy})

def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()
    
    correct_words = sum(o == t for o, t in zip(original_words, typed_words))
    total_words = len(original_words)
    
    return (correct_words / total_words) * 100

if __name__ == '__main__':
    app.run(debug=True)
