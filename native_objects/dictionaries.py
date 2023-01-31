# Dictionaries are something like hashes in Ruby

user = {}
user["first_name"] = "Elian"
user["last_name"] = "Braja"

user
{'first_name': 'Elian', 'last_name': 'Braja'}

#throws error is key is not found
user["first_name"]
"Elian"

#does not return error if key is not found
user.get("first_name")
"Elian"

user.keys()
user.values()

#Keys mund te konsiderohen si sets sepse ato nuk mund te mbajne vlera te dublikuara

"first_name" in user
True

user.items()
dict_items([('first_name', 'Elian'), ('last_name', 'Braja')])

for first_name, last_name in user.items():
    print(f"{first_name} {last_name}")