class rectangle:
    def __init__(self,w , l):
        self.weidth = w
        self.len = l
    def calculate_perimetr(self):
        return self.weidth + self.len
Rectangle = rectangle(8, 9)
print(Rectangle.calculate_perimetr())
class square:
    def __init__(self, w, l):
        self.w = w
        self.l = l
    def calculate_perimetr(self):
        return self.w*2 + self.l*2
    def change_size(self, w, l):
        self.w = w
        self.l = l
        return self.w * 2 + self.l * 2
Square = square(4, 4)
print(Square.calculate_perimetr())
Square.change_size(5, 7)
print(Square.calculate_perimetr())
class shape:
    def whatami(self):
        print("я фигура")

class horse():
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner
class person():
    def __init__(self, nam):
        self.name = nam
pawa = person("Pasha")
korova = horse("zalupa" , "vaflya", "pawa")
print(korova.owner.name)


