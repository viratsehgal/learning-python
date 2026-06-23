name = input("Enter your full name: ")
name_parts = name.split()
initials = ""
for part in name_parts:
    if initials:
        initials += "."
    initials += part[0].upper()
print(initials)
