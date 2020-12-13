import sys
import cmath

print("Input a:")
a = float(input())
print("Input b:")
b = float(input())
print("Input c:")
c = float(input())

if a == 0:
    print("a cannot be 0")
    sys.exit(1)

print(f"Equation is: y = {a}*x^2+{b}*x+{c}")

d = (b**2) - (4*a*c)
x1 = (-b-cmath.sqrt(d))/(2*a)
x2 = (-b+cmath.sqrt(d))/(2*a)
print(f"Soltuions are {x1} and {x2}")

