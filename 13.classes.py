# Python is an object oriented programming language

class Sample:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def display_name(self):
        print("your name is ", self.name)
    def display_id(self):
        print("your id is ", self.id)
    def display_info(self):
        print("your details are" , self.name , self.id)

s = Sample("Karan",1)
s.display_id()
s.display_info()
s.display_name()