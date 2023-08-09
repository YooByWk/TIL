def func3():
    print(3)
    return
def func2():
    func3()
    print(2)
    return
def func1():
    func2()
    print(1)
    return

func1()