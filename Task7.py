# Task 2: Word Frequency Counter (Basic)
# Write a Python program that takes a sentence from the user and counts how many times each word appears.

# Example:
# Input: python is easy and python is powerful

# Output:
# python: 2
# is: 2
# easy: 1
# and: 1
# powerful: 1

# Requirements:
# 1. Take a sentence as input.
# 2. Convert it into lowercase.
# 3. Split the sentence into words.
# 4. Use a dictionary to count word occurrences.
# 5. Display the dictionary.


text=input("Enter a sentence : ")
test=text.lower()
sentence=text.split()
word_count={}
for word in sentence:
    if word in word_count:
        word_count [word]+=1
    else:
        word_count[word]=1
print("Word Frequency : " , word_count)
