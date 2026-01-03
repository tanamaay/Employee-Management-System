import pytest
from app import create_app, db
from app.models import Employee
from app.repository.employee_repository import EmployeeRepository
from datetime import date

@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


def test_add_employee(app):
    emp = Employee(
        name="Jane",
        email="jane@test.com",
        department="HR",
        date_joined=date.today()
    )

    saved = EmployeeRepository.add(emp)

    assert saved.id is not None


def test_get_employee_by_email(app):
    emp = Employee(
        name="Sam",
        email="sam@test.com",
        department="Finance",
        date_joined=date.today()
    )

    EmployeeRepository.add(emp)

    found = EmployeeRepository.get_by_email("sam@test.com")
    assert found is not None
