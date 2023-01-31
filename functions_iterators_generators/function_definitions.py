def square(x):
    return x*x

square(5)
25

def squares_list(n):
    squares = []
    for i in range(n):
        squares.append(i**2)
    return squares

squares_list(11)

# Passing a function to another function
def function_adder(x, f):
    return f(x) + 1

function_adder(10, square)


def foo_args(*args):
    print(args)


def foo_kwargs(**kwargs):
    print(kwargs)


def foo_both(*args, **kwargs):
    print(args)
    print(kwargs)

foo_args("de", "wed")
('de', 'wed')


foo_kwargs(a= "de", b="wed")
{'a': 'de', 'b': 'wed'}

foo_both("a", "b", "c", test="e")
('a', 'b', 'c')
{'test': 'e'}




