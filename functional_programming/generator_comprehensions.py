# perfect square (the first square that contains all digits 0-9)

def has_all_digits(numbers):
    for n in numbers:
        if set(str(n)) == set("0123456789"):
            return n


# perfect square: Imperative version
def imperative_squares_generator():
    for n in range(10 ** 8 + 1):
        yield n ** 2

squares = imperative_squares_generator()
print(has_all_digits(squares))

# perfect square: Functional version (For generators we use () as comprehension instead of [])
squares = (n ** 2 for n in range(10 ** 8 + 1))
print(has_all_digits(squares))
