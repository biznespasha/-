class dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
class person:
    def __init__(self, name, secondname):
        self.name = name
        self.secondname = secondname
mick = person("Мик Джагер","pidoras")
stan = dog("стэнли", "залупа", mick)
print(stan.owner.secondnam)