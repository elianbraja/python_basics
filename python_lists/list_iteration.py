a = ["ant", "bat", "cat"]
for i in range(len(a)):
    print(a[i])

for e in a:
    print(e)

for i, e in enumerate(a):
    print(f"a[{i}] = {e}")


for i, e in enumerate(a):
    if e == "cat":
        print(f"Found the cat at index {i}!")
        break
    else:
        print(f"a[{i}] = {e}")