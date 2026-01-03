import pytest
from unittest.mock import patch, MagicMock
from app.service.employee_service import EmployeeService
from app.models import Employee
from datetime import date

# ---------- CREATE EMPLOYEE ----------

@patch("app.service.employee_service.EmployeeRepository")
def test_create_employee_success(mock_repo):
    mock_repo.get_by_email.return_value = None
    mock_repo.add.return_value = Employee(
        id=1,
        name="John",
        email="john@test.com",
        department="IT",
        date_joined=date.today()
    )

    data = {
        "name": "John",
        "email": "john@test.com",
        "department": "IT"
    }

    employee = EmployeeService.create_employee(data)

    assert employee.email == "john@test.com"


@patch("app.service.employee_service.EmployeeRepository")
def test_create_employee_duplicate_email(mock_repo):
    mock_repo.get_by_email.return_value = MagicMock()

    with pytest.raises(ValueError) as e:
        EmployeeService.create_employee({
            "name": "John",
            "email": "john@test.com",
            "department": "IT"
        })

    assert "Email already exists" in str(e.value)


# ---------- GET BY ID ----------

@patch("app.service.employee_service.EmployeeRepository")
def test_get_employee_not_found(mock_repo):
    mock_repo.get_by_id.return_value = None

    with pytest.raises(ValueError):
        EmployeeService.get_employee_by_id(99)


# ---------- DELETE ----------

@patch("app.service.employee_service.EmployeeRepository")
def test_delete_employee_success(mock_repo):
    mock_emp = MagicMock()
    mock_repo.get_by_id.return_value = mock_emp

    result = EmployeeService.delete_employee(1)

    assert result is True
    mock_repo.delete.assert_called_once()
