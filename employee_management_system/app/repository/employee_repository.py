from app.models import Employee
from app import db

class EmployeeRepository:

    @staticmethod
    def add(employee: Employee):
        db.session.add(employee)
        db.session.commit()
        return employee

    @staticmethod
    def get_all():
        return Employee.query.all()

    @staticmethod
    def get_by_id(employee_id):
        return Employee.query.get(employee_id)

    @staticmethod
    def get_by_email(email):
        return Employee.query.filter_by(email=email).first()

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(employee):
        db.session.delete(employee)
        db.session.commit()
