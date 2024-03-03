mystring = input("Input string: ")

mystring = mystring.replace(" ", "").lower()

if mystring == mystring[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")