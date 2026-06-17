import math

number_input = (float(input("Enter a number: ")))
if number_input > 0:
    square_root = math.sqrt(number_input)
    square = number_input ** 2
    cube = number_input ** 3
    print("The square root of the given number is " , square_root)
    print("The square of the given number is " , square)
    print("The cube of the given number is " , cube)
elif number_input == 0:
    print("Null")
elif number_input < 0:
    number_input = abs(number_input)
    square_root = math.sqrt(number_input)
    square = number_input ** 2
    cube = number_input ** 3
    print("The square root of the given number is " , square_root , "when number is converted into a positive")
    print("The square of the given number is " , square , "when number is converted into a positive")
    print("The cube of the given number is " , cube , "when number is converted into a positive")
