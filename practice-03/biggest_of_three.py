a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a == b == c:
    print(f"All three numbers are equal: {a}")
elif a == b and a > c:
    print(f"Both {a} and {b} are the largest")
elif a == c and a > b:
    print(f"Both {a} and {c} are the largest")
elif b == c and b > a:
    print(f"Both {b} and {c} are the largest")
elif a > b and a > c:
    print(f"{a} is the largest")
elif b > a and b > c:
    print(f"{b} is the largest")
else:
    print(f"{c} is the largest")
