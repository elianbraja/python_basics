states = ["Kansas", "Nebraska", "North Dakota", "South Dakota"]

# lengths: Imperative version
def imperative_lengths(states):
    lengths = {}
    for state in states:
        lengths[state] = len(state)
    return lengths

# lengths: Functional version
def functional_lengths(states):
    return {state: len(state) for state in states}

print(imperative_lengths(states))
print(functional_lengths(states))