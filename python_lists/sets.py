# Sets are similar to lists and touples. A set of elements with element in not a particular order
# and with no duplicates

s1 = {1, 2, 3, 4}
s2 = set([1, 2, 3, 3, 4, 4])
s2
{1, 2 ,3 ,4}

#sets union
s1 = {1, 2, "ant", "bat"}
s2 = {2, 3, "bat", "cat"}
s1 | s2
{1, 2, "bat", 3, "cat", "ant"}

#sets intersection
s1 = {1, 2, "ant", "bat"}
s2 = {2, 3, "bat", "cat"}
s1 & s2
{2, "bat"}