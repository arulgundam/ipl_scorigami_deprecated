from flask import Flask, render_template, jsonify

app = Flask(__name__)

def get_ipl_data():
    # Example data, replace with actual database query
    ipl_data = [
        {"first_innings_score": 180, "second_innings_score": 175, "wickets_fallen": 6},
        {"first_innings_score": 150, "second_innings_score": 140, "wickets_fallen": 8},
        {"first_innings_score": 200, "second_innings_score": 180, "wickets_fallen": 5},
        {"first_innings_score": 160, "second_innings_score": 165, "wickets_fallen": 7},
        {"first_innings_score": 170, "second_innings_score": 160, "wickets_fallen": 9},
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
