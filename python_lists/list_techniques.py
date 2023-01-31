a = [42, 30, 44, 4]

42 in a
True

# the sort method mutates the list, so it changes to the new list.
a.sort()
a
[4, 30, 42, 44]

a.reverse()
a
[44, 42, 30, 4]

# be aware of the case below. a2 is just pointing to an address in memory.
# when a1 changes, a2 does too.

a1 = [42, 30, 44, 4]
a2 = a1
a1.sort()

a1
[4, 30, 42, 44]

a2
[4, 30, 42, 44]

#To prevent the case on top we can use the copy method.
a1 = [42, 30, 44, 4]
a2 = a1.copy()
a1.sort()

a1
[4, 30, 42, 44]

a2
[42, 30, 44, 4]


#To prevent mutationg the original array
sorted(a)

#non-pythonic
a1 == a2
True

#pythonic
a1 is a2
True

#append, pop
a.append(6)
a
[42, 30, 44, 4, 6]

a.pop()
a
[42, 30, 44, 4]

#joining
a = ["ant", "bat", "cat"]
"".join(a)
'antbatcat'

" -- ".join(a)
'ant -- bat -- cat'







