import re
class square:
    def __init__(self, name):
        self.name = name

    def print_size(self):
        print(""" {} на {} на {} na {}""".format(self.name, self.name, self.name, self.name))
Square = square(20)
Square.print_size()

class person:
    def __init__(self):
        self.name = "asdas"
xuy = person()
same_bob = xuy
print(xuy is same_bob)
bob = person()
print(bob is xuy)


cntr = "Москва: 777, 999, 151. Тула: 754,348,444"
m = re.findall("\d", cntr, re.IGNORECASE,)
print(m)

slovo = "Приведение прошуршало и исчезло в углу"
s = re.findall(("\B[лозлоало]\w+"),slovo, re.MULTILINE)
print(s)
text = "Два, даа, давинчи, давай."
t = re.sub(r"два", "3" ,text,flags=re.I)
print(t)