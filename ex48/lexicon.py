def convert_num(s):
	try:
		return int(s)
	except ValueError:
		return None

			
def scan(raw):
	
	lexicon = [('direction','north'),
				('direction','south'),
				('direction','east'),
				('direction','west'),
				('direction','down'),
				('direction','up'),
				('direction','left'),
				('direction','right'),
				('verb','go'),
				('verb','stop'),
				('verb','kill'),
				('verb','eat'),
				('stop','the'),
				('stop','in'),
				('stop','of'),
				('stop','at'),
				('stop','it'),
				('stop','from'),
				('noun','door'),
				('noun','bear'),
				('noun','princess'),
				('noun','cabinet'),
				('area','castle'),
				('area','trail'),
				('area','woods')
				]

	
	words = raw.split()
	sentence = []
		
	for i in range(len(words)):
			
		location = 0;
		found = False
		j = 0;
			
		if convert_num(words[i]) == None:
				
			low_word = words[i].lower()
				
			while (j < len(lexicon)) and (found == False):
		
				found = lexicon[j].__contains__(low_word)
					
				if found == True:
					location = j
					
				j += 1
			
			if found == False:
			
				err = ('error', words[i])
				sentence.append(err)
				
			else:
				sentence.append(lexicon[location])
	
		elif convert_num(words[i]) != None:
				
			num = ('number', words[i])
			sentence.append(num)
				
	return sentence