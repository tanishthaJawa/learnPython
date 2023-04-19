employee_file = open("employees.txt", "w")
# print(employee_file.readline())
# print(employee_file.readlines()[1])
employee_file.write("\nKelly - Developer")

# for employee in employee_file.readlines():
#     print(employee)
employee_file.close()
