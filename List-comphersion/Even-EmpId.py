employee_ids = [101, 102, 103, 104, 105, 106, 107, 108]

even_ids = [emp_id for emp_id in employee_ids if emp_id % 2 == 0]

print(even_ids)