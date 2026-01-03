from flask import Blueprint, request, jsonify
from app.service.employee_service import EmployeeService

employee_bp = Blueprint('employee_bp', __name__)

def format_employee(e):
    """Helper function to format employee objects consistently."""
    return {
        "id": e.id,
        "name": e.name,
        "email": e.email,
        "department": e.department,
        "date_joined": str(e.date_joined)
    }

# POST /employees
@employee_bp.route('', methods=['POST'])
def add_employee():
    try:
        data = request.get_json()
        employee = EmployeeService.create_employee(data)
        return jsonify(format_employee(employee)), 201  # 201 Created
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# GET /employees
@employee_bp.route('', methods=['GET'])
def get_employees():
    employees = EmployeeService.get_all_employees()
    return jsonify([format_employee(e) for e in employees]), 200

# GET /employees/<id>
@employee_bp.route('/<int:emp_id>', methods=['GET'])
def get_employee(emp_id):
    try:
        employee = EmployeeService.get_employee_by_id(emp_id)
        return jsonify(format_employee(employee)), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

# PUT /employees/<id>
@employee_bp.route('/<int:emp_id>', methods=['PUT'])
def update_employee(emp_id):
    try:
        data = request.get_json()
        employee = EmployeeService.update_employee(emp_id, data)
        return jsonify(format_employee(employee)), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# DELETE /employees/<id>
@employee_bp.route('/<int:emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    try:
        EmployeeService.delete_employee(emp_id)
        return jsonify({"message": "Employee deleted successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
