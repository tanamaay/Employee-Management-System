from . import db
from datetime import date

class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    department = db.Column(db.String(50), nullable=False)
    date_joined = db.Column(db.Date, default=date.today)

    def __repr__(self):
        return f"<Employee {self.name}>"
