states = ["Kansas", "Nebraska", "North Dakota", "South Dakota"]

# States with single word. Imperative version
def imperative_singles(states):
    singles = []
    for state in states:
        if len(state.split()) == 1:
            singles.append(state)
    return singles


# States with single word. Functional version
def functional_singles(states):
    return [state for state in states if len(state.split()) == 1]

print(imperative_singles(states))
print(functional_singles(states))