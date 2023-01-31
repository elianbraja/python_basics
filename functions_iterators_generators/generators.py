# A generator is a special kind of iterator that uses a special operation called yield.
# The effect of yield is to produce each element of the sequence in turn.

def characters(string):
    for c in string:
        yield c


# Suppose we wanted to write a function to find numbers that contain all of the digits 0–9.
# One clever way of doing this is noting that the set() function.


def has_all_digits(numbers):
    for n in numbers:
        if set(str(n)) == set("0123456789"):
            return n


has_all_digits([1424872341, 1236490835741, 12341960523])
1236490835741


# Now let’s use our function to find the first perfect square with all of the digits 0–9.
# One way of doing this is to create a list using all the numbers up to some big number.
# Since we don’t know how high to go, let’s try a hundred million.

def squares_generator():
    for n in range(10 ** 8 + 1):
        yield n ** 2

squares = squares_generator()
has_all_digits(squares)
1026753849

