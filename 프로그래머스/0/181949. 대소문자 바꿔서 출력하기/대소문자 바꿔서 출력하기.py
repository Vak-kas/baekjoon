str = input()

for i in str:
    if i in "ABCDEFGHIZKLMNOPQRSTUVWXYZ":
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")