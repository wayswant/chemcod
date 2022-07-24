def f(x):
    def g(y):
        return y / x

    return g


eq = f(2)(10)

print(eq)


def divisor(x, y):
    return x / y


eq2 = divisor(10, 2)

print(eq2)


def q(x):
    return 'pertanyaan' + str(x) + ' !'

print(q(1))