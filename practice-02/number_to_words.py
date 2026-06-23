words =[
    "", "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen"
]

while True:
    user_input= (input("Enter a number between 1 and 19 (or quit): "))

    if user_input.lower() == "quit":
        print("Goodbye!!!")
        break
    
    if not user_input.isdigit() or not 1 <=int(user_input) <= 19:
        print("Please enter a number between 1 and 19")
        continue

    print(words[int(user_input)])