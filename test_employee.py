from employee import get_employee_details

def test_employee_name():
    details = get_employee_details()
    assert details["name"] == "John Doe"