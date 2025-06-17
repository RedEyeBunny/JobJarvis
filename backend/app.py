from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Job

app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../jobs.db'


db.init_app(app)

"""
# Create the database tables (run once)
with app.app_context():
    db.create_all()
"""
# Example route
@app.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([
        {
            'id': job.id,
            'company': job.company,
            'position': job.position,
            'application_date': job.application_date,
            'status': job.status,
            'source': job.source,
            'sentiment': job.sentiment
        }
        for job in jobs
    ])

@app.route('/jobs',methods=['POST'])
def add_jobs():
    data = request.get_json()
    new_job = Job(
        company=data['company'],
        position=data['position'],
        status=data.get['status','Applied']
    )
    db.session.add(ne)
if __name__ == '__main__':
    app.run(debug=True)
