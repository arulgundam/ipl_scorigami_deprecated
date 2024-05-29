from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ipl_data.db'
db = SQLAlchemy(app)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_innings_score = db.Column(db.String(255))
    second_innings_score = db.Column(db.String(255))

def load_data_to_db(csv_file):
    df = pd.read_csv(csv_file)
    matches_data = df.to_dict(orient='records')
    
    # Create all tables if they don't exist
    db.create_all()

    for match in matches_data:
        db.session.add(Match(first_innings_score=match['1st_inning_score'], 
                             second_innings_score=match['2nd_inning_score']))
    db.session.commit()


@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    matches = Match.query.all()
    ipl_data = [{"first_innings_score": match.first_innings_score, 
                  "second_innings_score": match.second_innings_score} 
                 for match in matches]
    return jsonify(ipl_data)

if __name__ == '__main__':
    with app.app_context():
        load_data_to_db('all ipl seasons (completed matches only).csv')
    app.run(debug=True)
