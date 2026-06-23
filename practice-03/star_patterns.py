n = int(input("Enter a number between 1 and 9: "))

for i in range(1, n + 1):
    print("* " * i)
print()

for i in range(n, 0, -1):
    print("* " * i)
print()

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()