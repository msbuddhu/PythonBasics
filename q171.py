def decor(func):
    def inner(name):
        print("First Decor(decor) Function Execution")
        func(name)
    return inner
def decor1(func):
    def inner(name):
        print("First Decor(decor1) Function Execution")
        func(name)
    return inner
@decor1
@decor
def wish(name):
    print("Hello",name,"Good Morning")
wish("Durga")