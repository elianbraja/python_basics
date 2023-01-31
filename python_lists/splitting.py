"ant bat cat".split(" ")
["ant", "bat", "cat"]

"ant,bat,cat".split(",")
["ant", "bat", "cat"]

"antheybatheycathey".split("hey")
["ant", "bat", "cat"]

s = "This is a line.\nAnd this is another line."
s.split("\n")
['This is a line.', 'And this is another line.']

s.splitlines()
['This is a line.', 'And this is another line.']

#in python we cannot split an empty string to get the list of characters like we do in other languages
#instead use list

list("elian")
['e', 'l', 'i', 'a', 'n']



