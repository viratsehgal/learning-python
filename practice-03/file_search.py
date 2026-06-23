def search_notes(filename="notes.txt"):
    search_word = input("Enter a word to search for: ").strip()

    found = False
    line_number = 0
    with open (filename, "r") as file:
        for line in file:
            line_number += 1
            if search_word.lower() in line.lower():
                print(f"Line {line_number}: {line.strip()}")
                found = True
    
    if not found:
        print(f"No lines matched '{search_word}'. Try a different word!")

if __name__ == "__main__":
    search_notes()