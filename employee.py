def get_employee_details():
    return {
        "name": "John Doe",
        "position": "Software Engineer",
        "department": ["IT", "Development"],
        "salary": 80000
    }

if __name__ == "__main__":
    details = get_employee_details()
    print("Employee Name:", details["name"])
    print("Position:", details["position"])
    print("Department:", details["department"])
    print("Salary:", details["salary"])