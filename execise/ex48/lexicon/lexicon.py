#-*-utf-8-*-
direction=["north", "south", "east", "west", "down", "up", "left", "right", "back"]
verbs=["go", "stop", "kill", "eat"]
stop=["the", "in", "of", "from", "at", "it"]
nouns=["door", "bear", "princess", "cabinet"]
numbers=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def scan(input):
	words=input.split()
	ret=[]
	for word in words:
		if word in direction:
			ret.append(("direction", word))
		elif word in verbs:
			ret.append(("verb", word))
		elif word in stop:
			ret.append(("stop", word))
		elif word in nouns:
			ret.append(("noun", word))
		elif convert_number(word):
			ret.append(("number", word))
		else: 
			ret.append(("error", word))
	return ret
	
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
			