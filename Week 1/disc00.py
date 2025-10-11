def f(x):
    return x - 1
def g(x):
    return (x + 1) * 2
def h(x, y):
    return int(str(x) + str(y))

a = h(g(f(g(f(5)))), f(g(g(5))))
print(a)