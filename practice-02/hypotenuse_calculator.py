import math

print("Enter the sides of a right-angled triangle ")
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))

c = math.sqrt((math.pow(a, 2) + math.pow(b, 2)))

print(f"Hypotnuse: {round(c, 4)}")