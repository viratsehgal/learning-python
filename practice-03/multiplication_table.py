n = int(input("Enter the number of rows (n): "))
r = int(input("Enter the range limit (r): "))

width = len(str(n * 2)) + 2

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j :> {width}}" , end="")
    print()