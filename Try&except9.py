class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in range(5000,1500)range"):
       self.salary = salary
       self.message = message
       super().__init__(message)

####1. Normal Execution:

# salary = int(input("Enter salary amount: "))
# if not 5000 < salary < 15000:
#     raise SalaryNotInRangeError(salary)

##### 2.To deal with try and except

try:
    salary = int(input("Enter salary amount: "))
    if not 5000 < salary < 15000:
     raise SalaryNotInRangeError(salary)

except SalaryNotInRangeError :
    print("You just crossed the limit")