def doc():
    return "Получить легковую машину"
def udo():
    return "Получить грузовую"
def kat():
    return "Получить автобус"
def gai(kategoriya):
    if kategoriya == "a":
        return doc()
    elif kategoriya  == "b":
        return udo()
    elif kategoriya == "c":
        return kat()
print(gai("c"))