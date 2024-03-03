mystring = input("Input string: ")

upper = 0
lower= 0

upper = sum(1 for c in mystring if c.isupper())
lower = sum(1 for c in mystring if c.islower())

print("Count of uppercase letters: ", upper)
print("Count of lowercase letters: ", lower)