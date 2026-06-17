user_input = input("Enter a word: ")
input_reverse = user_input[::-1]

if user_input == input_reverse:
    print("The word", user_input, "is a palindrome")
else:
    print("The word", user_input, "is not a palindrome")
