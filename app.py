from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

def get_ipl_data():
    # Generate 100 random scores between 40 and 300 for first innings and second innings
    ipl_data = [
        {"first_innings_score": random.randint(40, 300), "second_innings_score": random.randint(40, 300)}
        for _ in range(100)  # Generate 100 matches' data
    ]
    return ipl_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    ipl_data = get_ipl_data()
    return jsonify(ipl_data)

if __name__ == '__main__':
    app.run(debug=True)