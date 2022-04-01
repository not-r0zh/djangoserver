from django.http import HttpResponse
from django.shortcuts import render
import operator
import random

def pollofrito(request):
	print(request)
	nombres = ["pepe","juan","miguel"]
	nombre = random.choice(nombres)
	return render(request,'templatetest.html',{'nombre':nombre})

def home(request):
	return render(request,'home.html')


def count(request):
	fulltext = request.GET['fulltext']
	variable1 = ""
	variable2 = ""
	wordlist = fulltext.split()
	
	if len(wordlist)==1:
		variable1 = "is"
		variable2 = "word"
	else:
		variable1 = "are"
		variable2 = "words"
	
	worddictionary = {}

	for word in wordlist:
		if word in worddictionary:
			#Increase
			worddictionary[word] += 1
		else:
			#add to the dictionary
			worddictionary[word] = 1

	sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)


	return render(request,'count.html',{'fulltext':fulltext, 'count':len(wordlist),'sortedwords':sortedwords,'variable1':variable1,'variable2':variable2})

def about(request):
	return render(request,'about.html')