sentence = input("Enter a sentence: ")

words = sentence.split()
sentence_count = sentence.count(".") + sentence.count("?") + sentence.count("!")
longest_word = max(words , key=len)

print("The lenght of the sentence is" , len(sentence))
print("The number of words in the sentence is" , len(words))
print("The total number of sentences typed is" , sentence_count)
print("The longest word in the sentence is" , longest_word)