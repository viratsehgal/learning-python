num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
num3 = float(input("Enter a number: "))
num4 = float(input("Enter a number: "))
num5 = float(input("Enter a number: "))
num6 = float(input("Enter a number: "))
num7 = float(input("Enter a number: "))
num8 = float(input("Enter a number: "))

entered_numbers = [num1 ,num2 ,num3 ,num4 ,num5 ,num6 ,num7 ,num8]

highest_number = max(entered_numbers)
lowest_number = min(entered_numbers)
average = sum(entered_numbers) / len(entered_numbers)
ascending_order = sorted(entered_numbers)

print("Highest number in the list is:" , highest_number)
print("Lowest number in the list is:" , lowest_number)
print("Average of all the numbers in the list is:" , average)
print("The list in ascending order:" , ascending_order)