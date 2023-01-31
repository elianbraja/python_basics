#Python supports tuples, which are basically lists that can't be changed.

t = ("fox", "dog", "eel")
t
('fox', 'dog', 'eel')

#we can use methods like we do with lists expects of those methods that mutate.
sorted(t)
['dog', 'eel', 'fox']

#this mthod cannot be applied on touples
t.sort()

