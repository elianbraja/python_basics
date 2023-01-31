states = ["Kansas", "Kansas", "Nebraska", "North Dakota", "South Dakota"]


def urlify(string):
    """Return a URL-friendly of a string."""
    return "-".join(string.lower().split())


# urls: Imperative version
def imperative_urls(states):
    urls = set()
    for state in states:
        urls.add(urlify(state))
    return urls


# urls: Functional version
def functional_urls(states):
    return {urlify(state) for state in states}


print(imperative_urls(states))
print(functional_urls(states))
