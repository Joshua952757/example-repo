# user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hair_color = input("Enter your hair color: ")
eye_color = input("Enter your eye color: ")
# initiating parent class
class Adult:
    def __init__(self, name, age, eye_color, hair_color):
        self.name = name
        self.age = age
        self.eye_color = eye_color
        self.hair_color = hair_color
    
    def can_drive(self):
        print(self.name, "is old enough to drive.")
# adding sub-class
class Child(Adult):
    def can_drive(self):
        print(self.name, "is too young to drive.")
# evaluating user age input
if age >= 18:
    person = Adult(name, age, eye_color, hair_color)
else:
    person = Child(name, age, eye_color, hair_color)

person.can_drive()
