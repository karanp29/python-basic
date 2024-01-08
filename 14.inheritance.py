class Shape:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        raise Exception("child class must implement this method")
    def compare(self, other_area):
        if self.area() > other_area.area():
            print("this is larger")
        else:
            print("this is smaller")

class Rectangle(Shape):
    def area(self):
        return self.length * self.width

r = Rectangle(10,2)
r1 = Rectangle(10,3)
print (r.area())
r.compare(r1)