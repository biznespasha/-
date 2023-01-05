def decor(f):
    def wrapper():
        try:
            h = f()
        except Exception:
            print('repeat enter...')
            h = f()
        return h
    return wrapper


@decor # make = decor(make)
def make():
    enter = float(input("vvedi"))
    return enter
@decor
def make2():
    enter = float(input('vveditee opa0tb'))
    return enter

make2()
make()