numbers = range(1, 101)

# sum: Imperative version
def imperative_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

# sum: Imperative version
def functional_sum(numbers):
    return sum(numbers)

print(imperative_sum(numbers))
print(functional_sum(numbers))