from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# 문장 목록
texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an easy-to-learn programming language.",
    "Data science is a multidisciplinary field.",
    "Artificial intelligence is transforming many industries.",
    "Natural language processing involves understanding human language."
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
