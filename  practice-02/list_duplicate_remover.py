words = []
for i in range(1, 11):
    word = input(f"Enter word {i}: ")
    words.append(word)

print("Original list:", words)

cleaned = []
for word in words:
    if word not in cleaned:
        cleaned.append(word)

print("Cleaned list (duplicates removed):", cleaned)