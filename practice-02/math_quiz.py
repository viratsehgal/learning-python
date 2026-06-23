import random

score = 0

for i in range(1, 6):
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    answer = int(input(f"Question {i}: What is {num1} + {num2} ? :"))
    if answer == num1 + num2:
        print("Correct")
        score += 1
    else:
        print(f"Wrong! the answer was {num1 + num2}.")

print(f"You scored {score} out of 5.")