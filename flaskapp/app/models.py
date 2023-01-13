from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from datetime import datetime

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    creatorId = db.Column(db.Integer,nullable=False)
    title = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    subcategory = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    imageurl = db.Column(db.String(255), nullable=False)
    videourl = db.Column(db.String(50))
    fundingGoal = db.Column(db.Numeric,nullable=False)
    startDate = db.Column(db.String(50), nullable=False)
    endDate = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    risk = db.Column(db.String(1000), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)
    budget = db.Column(db.Numeric, nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.now)
    updatedAt = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def to_dict(self):
      return {
        'id': self.id,
        'title': self.title,
        'category': self.category,
        'subcategory': self.subcategory,
        'city': self.city,
        'state': self.state,
        'country': self.country,
        'fundingGoal': self.fundingGoal,
        'startDate': self.startDate,
        'endDate': self.endDate,
        'description': self.description,
        'risk': self.risk,
        'budget': self.budget,
        'status': self.status,
        'createdAt': str(self.createdAt),
        'updatedAt': str(self.updatedAt)
      }