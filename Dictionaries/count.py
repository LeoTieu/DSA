import re
# Count all words in a text file
# Cheated with ChatGPT

word_count = {}

with open("Dictionaries/ai.txt", 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().lower() # Remove leading/trailing whitespaces and convert to lowercase
        line = re.sub(r'[^a-z ]+', '', line) # Remove non-alphabetic characters
        line = line.split()
        for word in line:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    
print(word_count)
