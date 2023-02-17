class Student:
    def __init__(self,name,place,age):
        self.name = name
        self.place = place
        self.age = age

    def set_age(self,age_new):
        self.age = age_new
        print("Your age is set as", self.age)

    def get_age(self):
        print("Your age is", self.age) 

    def display_student_details(self):
        print("Name:", self.name)
        print("Place:", self.place)
        print("Age:", self.age)       
                    