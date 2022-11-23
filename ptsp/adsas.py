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
Square = square(4, 4)
print(Square.calculate_perimetr())