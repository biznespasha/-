import math

class Circle:
    def __init__(self,r , p):
        self.radius = r
        self.pi = p
    def area(self):
        return self.radius**2 * math.pi
circle = Circle(12, math.pi)
print(circle.area())

class Triangle:
    def __init__(self, a , b, s):

        self.akatet = a
        self.bkatet = b
        self.skatet = s
    def area(self):
        return  self.akatet * self.bkatet / self.skatet
triangle = Triangle (10, 4 , 2)
print(triangle.area())
class Hexogon:
    def __init__(self,q,w,e,r,t,y,):
        self.q = q
        self.w = w
        self.e = e
        self.r = r
        self.t = t
        self.y = y
    def calculate_perimetr(self):
        return self.q + self.w + self.e + self.r + self.t +self.y
hexogon = Hexogon (2,3,5,1,3,4)
print(hexogon.calculate_perimetr())

