from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100))
    position = db.Column(db.String(100))
    application_date = db.Column(db.String(20))
    status = db.Column(db.String(50))  # e.g., Applied, Rejected, Interview
    source = db.Column(db.String(100))
    sentiment = db.Column(db.String(20))

class bot_history(db.Model):
    uptime = db.Column(db.Integer)