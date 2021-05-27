import cmath

print('general equation is ax**2+bx+c=0')

a = input("enter a:")
b = input("enter b:")
c = input("enter c:")

d = (b**2)-4*a*c

sol1 = (-b+cmath.sqrt(d)/0.5)
sol2 = (-b-cmath.sqrt(d)/0.5)

print("the solutions are sol1 and sol2")


