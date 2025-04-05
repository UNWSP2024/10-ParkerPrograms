# Nathan Parker
# 04/04/25
# Program #4 Employee Class



# Create a class
class Employee:

    # The __init__ method accepts name, ID_number, department, and job_title and assigns them to data attributes
    def __init__(self, name, ID_number, department, job_title):
        self.__name = name
        self.__ID_number = ID_number
        self.__department = department
        self.__job_title = job_title

    # The set_name method sets the __name instance attribute to the name
    def set_name(self, name):
        self.__name = name

    # The set_ID_number method sets the __ID_number instance attribute to the ID_number
    def set_ID_number(self, ID_number):
        self.__ID_number = ID_number

    # The set_department method sets the __department instance attribute to the department
    def set_department(self, department):
        self.__department = department

    # The set_job_title method sets the __job_title instance attribute to the job_title
    def set_job_title(self, job_title):
        self.__job_title = job_title

    # The get_name method returns the value referenced by __name
    def get_name(self):
        return self.__name

    # The get_ID_number method returns the value referenced by __ID_number
    def get_ID_number(self):
        return self.__ID_number

    # The get_department method returns the value referenced by __department
    def get_department(self):
        return self.__department

    # The get_job_title method returns the value referenced by __job_title
    def get_job_title(self):
        return self.__job_title



# define the main function
def main():

    # Create an object from the Employee class
    employee_1 = Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')

    # Create a second object from the Employee class
    employee_2 = Employee('Mark Jones', '39119', 'IT', 'Programmer')

    # Create a third object from the Employee class
    employee_3 = Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')

    # Display the attributes of the objects
    for employee_num in (employee_1,employee_2,employee_3):
        print(f'''
Name: {employee_num.get_name()}
ID Number: {employee_num.get_ID_number()}
Department: {employee_num.get_department()}
Job Title: {employee_num.get_job_title()}''')

# Call the main function
if __name__ == '__main__':
    main()

