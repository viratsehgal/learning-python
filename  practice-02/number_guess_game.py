secret_number = 67
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print("CORRECT GUESS!!","Number of attempts =",attempts)
        break
    elif guess > secret_number:
        print("Higher!!")
    elif guess < secret_number:
        print("Lower!!")