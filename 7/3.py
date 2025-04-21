empdata = {
    'HR': {'emp1': 5000, 'emp2': 6000},
    'IT': {'emp3': 7000, 'emp4': 8000},
    'Sales': {'emp5': 4000, 'emp6': 5500}
}

for dept, employees in empdata.items():
    minsalary = min(employees.values())
    maxsalary = max(employees.values())
    print(f"{dept} - Min Salary: {minsalary}, Max Salary: {maxsalary}")
