
a = input("Wpisz słowo a ja powiem czy to palindrom: ")

def palindrom(a):
    a = a.lower()
if a[::-1] == a:
    print("Tak to palindrom")
else:
    print("To nie palindrom")
