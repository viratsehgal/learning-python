while True:
    score = int(input("Enter a score between (0-100) to grade: "))

    if 0 <= score <= 100:

        if score >= 90:
            print("Your score is: A")
        elif 80 <= score < 90:
            print("Your score is: B")
        elif 70 <= score < 80:
            print("Your score is: C")
        elif 60 <= score < 70:
            print("Your score is: D")
        elif 0 <= score < 60:
            print("Your score is: F")
        break
    else:
        print("Enter a valid score")