from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

def get_ipl_data():
    # Generate repeated dummy data with occurrences
    ipl_data = [
        {"first_innings_score": random.randint(40, 300), "second_innings_score": random.randint(40, 300)}
        for _ in range(100)  # Generate 100 matches' data
    ]
    
    # Add occurrences based on repeated scores
    score_counts = {}
    for match in ipl_data:
        score = (match['first_innings_score'], match['second_innings_score'])
        if score in score_counts:
            score_counts[score] += 1
        else:
            score_counts[score] = 1
    
    # Merge data with occurrences
    ipl_data_with_occurrences = []
    for match in ipl_data:
        score = (match['first_innings_score'], match['second_innings_score'])
        occurrences = score_counts[score]
        match_with_occurrences = match.copy()
        match_with_occurrences['occurrences'] = occurrences
        ipl_data_with_occurrences.append(match_with_occurrences)
    
    return ipl_data_with_occurrences

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    ipl_data = get_ipl_data()
    return jsonify(ipl_data)

if __name__ == '__main__':
    app.run(debug=True)
