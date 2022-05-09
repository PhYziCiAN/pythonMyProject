class Dog:  # Defining the class
    """A simple attempt to model a dog."""  # Doc string describing the class

    def __init__(self, name, age):  # Special method that Python runs automatically when a new instance is created.
        # Self must be the first variable in this function
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


my_dog = Dog("willie", 6)  # Telling python to create the dog named willie who is 6.
my_dog.sit()
my_dog.roll_over()
print("My dog's name is " + my_dog.name.title() + ".")  # Accessing the value of the variable created
print("My dog is " + str(my_dog.age) + " years old.")  # Accessing the value of the 2nd variable
