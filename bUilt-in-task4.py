import time, math

n = int(input("Input number: "))
d = int(input("Input delay: "))

time.sleep(d / 1000)

sqrtn = math.sqrt(n)

print(f"Square root of {n} after {d} miliseconds is {sqrtn}")