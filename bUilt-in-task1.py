list_numbers = input("Input list elements with space between").split()
c = 1
for x in list_numbers:
    c *= int(x)

print("Result of multiplication: ", c)