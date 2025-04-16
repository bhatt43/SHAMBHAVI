employees = [
    {'dept': 'HR', 'roll': 101, 'salary': 50000},
    {'dept': 'HR', 'roll': 102, 'salary': 55000},
    {'dept': 'IT', 'roll': 201, 'salary': 70000},
    {'dept': 'IT', 'roll': 202, 'salary': 65000},
    {'dept': 'Finance', 'roll': 301, 'salary': 60000},
    {'dept': 'Finance', 'roll': 302, 'salary': 62000}
]

dept_salaries = {}

for emp in employees:
    dept = emp['dept']
    salary = emp['salary']
    if dept not in dept_salaries:
        dept_salaries[dept] = []
    dept_salaries[dept].append(salary)

for dept, salaries in dept_salaries.items():
    min_salary = min(salaries)
    max_salary = max(salaries)
    print(f"Department: {dept}")
    print(f"  Minimum Salary: {min_salary}")
    print(f"  Maximum Salary: {max_salary}")
