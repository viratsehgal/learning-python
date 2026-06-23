first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your birth year: "))

person = (first_name, last_name, birth_year)

first, last, birth = person

age = 2025 - birth
print(f"Hello, {first} {last}! You were born in {birth} and are {age} years old.")
