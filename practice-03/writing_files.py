import os

name = input("Enter your name: ")

goals = []
for i in range(1, 4):
    goal = input(f"Enter goal {i}: ")
    goals.append(goal)

with open("goals.txt", "a") as f:
    if os.path.exists("goals.txt"):
        f.write("\n")
    f.write(f"===== Goals for {name} =====\n")
    for i in range(len(goals)):
        f.write(f"  {i + 1}. {goals[i]}\n")
    f.write("=" * (len(name) + 24) + "\n")

with open("goals.txt", "r") as f:
    print("\n--- File Contents ---")
    print(f.read())
    print("--- End of File ---")