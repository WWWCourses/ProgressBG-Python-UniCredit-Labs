sentence = """
	apple and banana one apple one banana
	a red apple and a green apple
"""

sentence = sentence.strip()
words = sentence.split(sep=' ')

words_count = {}
unique_words = set(words)
print( unique_words )

for word in unique_words:
	words_count[word] = 0

for word in words:
	words_count[word] += 1

print(words_count)





