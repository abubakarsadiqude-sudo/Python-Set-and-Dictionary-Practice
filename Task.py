# reate a Python program that takes a sentence from the user and performs the following operations:
# 1. Convert the sentence into lowercase.
# 2. Split the sentence into individual words.
# 3. Store all words in a set to remove duplicates.
# 4. Display the total number of words.
# 5. Display the number of unique words.
# 6. Display all unique words in alphabetical order.
# 7. Ask the user to enter a word and check whether it exists in the sentence.

sentence = input("Enter a sentence: ")

sentence = sentence.lower()

words = sentence.split()

unique_words = set(words)

print("Total Words:", len(words))

print("Unique Words:", len(unique_words))

print("Unique Words in Alphabetical Order:")

for word in sorted(unique_words):
    print(word)

search_word = input("Enter a word to search: ").lower()

if search_word in unique_words:
    print("Word is present in the sentence.")
else:
    print("Word is not present in the sentence.")