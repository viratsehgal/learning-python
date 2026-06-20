total = 0
count = 0
while True:
    entry = input("Enter a number (or 'done' to finish): ")
    if entry == "done" :
        break
    try:
        total += int(entry)
        count += 1
        print("running total :" , total)
    except:
        print("Invalid input. Please enter a number or 'done'")

print("Final total:" , total)
print("Final count:" , count)