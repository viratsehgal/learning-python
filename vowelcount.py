#Vowel count

def vowel_count(phrase) : 
  count = 0
  for i in phrase:
    if i in "AEIOUaeiou":
      count += 1
  return count

print(vowel_count(input("Enter a sentence: ")))