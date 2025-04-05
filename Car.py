# Nathan Parker
# 04/04/25
# Program #2: Car Class



# Create a class
class Car:

    # The __init__ method accepts year_model and make and assigns them to data attributes
    # The __init__ method also creates the speed attribute and sets it to 0
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # The accelerate method adds 5 to the speed
    def accelerate(self):
        self.__speed += 5

    # The brake method subtracts 5 from the speed
    def brake(self):
        self.__speed -= 5

    # The get_speed method returns the speed
    def get_speed(self):
        return self.__speed



# define the main function
def main():

    # Get the year and model from the user
    car_year_model = input('Enter the year and model of the car: ')

    # Get the make from the user
    car_make = input('Enter the make of the car: ')

    # Create an object from the car class
    car = Car(car_year_model, car_make)

    # Call the accelerate method and the get_speed method 5 times
    print('Accelerating...')
    for loop in range(5):
        car.accelerate()
        print(f'The current speed is {car.get_speed()}.')

    # Call the brake method and the get_speed method 5 times
    print('Braking...')
    for loop in range(5):
        car.brake()
        print(f'The current speed is {car.get_speed()}.')

# Call the main function
if __name__ == '__main__':
    main()

