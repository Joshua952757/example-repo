class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)
    
    def head_office(self):
        print("Head office is located in Cape Town.")
# initiating sub-class
class OOPCourse(Course):
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"
    
    def trainer_details(self):
        print("Course description:", self.description)
        print("Trainer:", self.trainer)
    
    def show_course_id(self):
        print("Course ID: #12345")

# Object for OOPCourse
course_1 = OOPCourse()

# Method calling
course_1.contact_details()
course_1.head_office()
course_1.trainer_details()
course_1.show_course_id()