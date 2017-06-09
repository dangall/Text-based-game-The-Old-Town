import random
import math
from nltk.corpus import wordnet as wn

def findsynonyms(word):
	synonlist = wn.synsets(word)
	totalsyns = []
	
	for syn in synonlist:
		#this merges the two lists together
		totalsyns = totalsyns + syn.lemma_names()
	
	#Now remove the duplicates
	totalsyns = list(set(totalsyns))
	#Now make underscores become spaces
	for i,syn in enumerate(totalsyns):
		totalsyns[i] = syn.replace('_', ' ')
		
	return totalsyns

def yesno(word): #tells you whether the user answered yes or not
	done=0
	newword = word
	while done==0:
		if (newword == "yes" or newword == "Yes" or newword == "y" 
			or newword == "Y" or newword == "Yeah" or newword == "yeah" 
			or newword == "yep" or newword == "Yep"):
			done = 1
			return "yes"
		elif (newword == "no" or newword == "No" or newword == "n" 
			  or newword == "N" or newword == "Nah" or newword == "nah" 
			  or newword == "nope" or newword == "Nope"):
			done = 1
			return "no"
		else:
			newword = dontunderstand()
			
		
def dontunderstand():
	possiblephrases = ["\nI didn't understand, could you repeat it differently?\n",
					   "\nCould you use different words?\n",
					   "\nWould you mind paraphrasing that?\n",
					   "\nYou might not be able to do what you're trying to do. Try something else:\n"]
	print possiblephrases[random.randint(0,len(possiblephrases)-1)]
	newanswer = raw_input("> ")
	return newanswer

def asktoget(compwords): #This functions asks the user for an input and
						 #checks if it is a synonym of any of the compwords
	done=0
	sentence = raw_input("> ")
	while done==0:
		wordlist = sentence.split()
		allsynons = []
		for wad in wordlist:
			allsynons = allsynons + findsynonyms(wad)
	
		allsynons = allsynons + [sentence] 
		allsynons = list(set(allsynons)) + wordlist
		#print "allsynons:"
		#print allsynons
		#get the intersection of the two lists
		intersec = [val for val in compwords if val in allsynons]
		if intersec==[]:
			sentence = dontunderstand()
		else:
			done = 1
		
	return intersec
	
def distance(p1, p2): #computes the distance between coords p1 and p2
		return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def walk(pers, endlocation, time):
	timeleft = time - math.hypot(endlocation.coord[0] - pers.location.coord[0], endlocation.coord[1] - pers.location.coord[1])
	print "\nYou just walked %d meters.\n" % (100*math.hypot(endlocation.coord[0] - pers.location.coord[0], endlocation.coord[1] - pers.location.coord[1]))
	pers.location = endlocation
	endlocation.arrive()
	return timeleft
	
def intersect(list1, list2):
	return [val for val in list1 if val in list2]

		
		
		
	



	
	
