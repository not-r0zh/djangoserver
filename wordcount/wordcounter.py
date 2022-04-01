import string
import random

wordlist=[]

for i in range(1,10):
	wordlist.append(random.choice(string.ascii_letters))

worddictionary = {}

for word in wordlist:
	if word in worddictionary:
		worddictionary[word] += 1

	else:
		worddictionary[word] = 1
print(wordlist)
print(worddictionary)