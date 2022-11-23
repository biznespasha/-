class Apple:
    def __init__(self, c, w, h, l):
        self.color = c
        self.weight = w
        self.health = h
        self.look = l
app = Apple
app.color = "green"
app.weight = 7.5
app.health = 100
app.look = "good"
print("создано")
print(app.look)
print((app.color))
print(app.weight)
print(app.health)
