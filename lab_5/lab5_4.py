text = input()
word = input()
word_index = 0
word_len = len(word)

for char in text:
    if word_index < word_len and char == word[word_index]:
        word_index += 1

print(word_index == word_len)
