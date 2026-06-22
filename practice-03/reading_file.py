with open("diary.txt", "r") as file:
    lines = file.readlines()

total_lines = len(lines)

total_words = 0
longest_line = ""
longest_line_number = 0

for i in range(len(lines)):
    words = lines[i].split()
    total_words += len(words)

    if len(lines[i]) > len(longest_line):
        longest_line = lines[i]
        longest_line_number = i + 1

print(f"Total number of lines: {total_lines}")
print(f"Total number of words: {total_words}")
print(f"Longest line (line {longest_line_number}): {longest_line.strip()}")
