from app.models import Employee
from app.repository.employee_repository import EmployeeRepository
from datetime import datetime

class EmployeeService:

    @staticmethod
    def create_employee(data):
        # Validation
        if not all(k in data for k in ("name", "email", "department")):
            raise ValueError("Missing required fields")

        if EmployeeRepository.get_by_email(data['email']):
            raise ValueError("Email already exists")

        employee = Employee(
            name=data['name'],
            email=data['email'],
            department=data['department'],
            date_joined=datetime.strptime(data.get('date_joined', datetime.today().strftime('%Y-%m-%d')), '%Y-%m-%d').date()
        )

        return EmployeeRepository.add(employee)

    @staticmethod
    def get_all_employees():
        return EmployeeRepository.get_all()

    @staticmethod
    def get_employee_by_id(emp_id):
        employee = EmployeeRepository.get_by_id(emp_id)
        if not employee:
            raise ValueError("Employee not found")
        return employee

    @staticmethod
    def update_employee(emp_id, data):
        employee = EmployeeRepository.get_by_id(emp_id)
        if not employee:
            raise ValueError("Employee not found")

        if 'name' in data:
            employee.name = data['name']
        if 'email' in data:
            # Check duplicate email
            if EmployeeRepository.get_by_email(data['email']) and EmployeeRepository.get_by_email(data['email']).id != emp_id:
                raise ValueError("Email already exists")
            employee.email = data['email']
        if 'department' in data:
            employee.department = data['department']
        if 'date_joined' in data:
            employee.date_joined = datetime.strptime(data['date_joined'], '%Y-%m-%d').date()

        EmployeeRepository.update()
        return employee

    @staticmethod
    def delete_employee(emp_id):
        employee = EmployeeRepository.get_by_id(emp_id)
        if not employee:
            raise ValueError("Employee not found")
        EmployeeRepository.delete(employee)
        return True
