pip install flask flask_sqlalchemy flask_cors
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/flightstatus'
db = SQLAlchemy(app)
CORS(app)

class FlightStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    gate = db.Column(db.String(10))
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/api/status', methods=['GET'])
def get_status():
    flight_number = request.args.get('flight_number')
    status = FlightStatus.query.filter_by(flight_number=flight_number).first()
    if status:
        return jsonify({
            'flight_number': status.flight_number,
            'status': status.status,
            'gate': status.gate,
            'updated_at': status.updated_at
        })
    else:
        return jsonify({'message': 'Flight not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
#initialize db
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
