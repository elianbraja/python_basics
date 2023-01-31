#defining length
len("hello, world!")
13

len("badger") < 10
True

#Not fully Pythonic
password = "foo"
if (len(password) < 6):
    print("Password is too short.")

"Password is too short."

#Pythonic
password = "foo"
if len(password) < 6:
    print("Password is too short.")

"Password is too short."


#if and else
password = "foobar"
if len(password) < 6:
     print("Password is too short.")
else:
    print("Password is long enough.")

"Password is long enough."


#elif
password = "goldilocks"
if len(password) < 6:
    print("Password is too short.")
elif len(password) < 50:
    print("Password is just right!")
else:
    print("Password is too long.")

"Password is just right!"


#Conditions
x = "foo"
y = ""

if x or y:
    print("At least one of the strings is nonempty.")
else:
    print("Both strings are empty!")

"At least one of the strings is nonempty."