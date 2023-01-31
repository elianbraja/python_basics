#string concatenation
print("foo" + "bar")

# Multiple strings can be concatenated at once.
print("ant" + "bat" + "cat")

# Not Pythonic
first_name = "Michael"
last_name = "Hartl"
print(first_name + " " + last_name)
'Michael Hartl'

# Pythonic
f"{first_name} is my first name."
'Michael is my first name.'

f"{first_name} {last_name}"
'Michael Hartl'

#Raw strings
# this in helpful in cases you want to print special caracters inside the string like "/n" or "/t". It prints
# exactly what you type
r"{first_name} {last_name}"
'{first_name} {last_name}'

r'Newlines (\n) and tabs (\t) both use the backslash character: \.'
'Newlines (\\n) and tabs (\\t) both use the backslash character: \\.'