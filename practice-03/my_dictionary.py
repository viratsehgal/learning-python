person = {
    "name": input("Enter your name: "),
    "age": input("Enter your age: "),
    "colour": input("Enter your favourite colour: ")
}
for key, value in person.items():
    print(f"{key:8}: {value}")