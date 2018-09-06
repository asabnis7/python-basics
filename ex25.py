def break_words(line):
	"""Function breaks lines"""
	words = line.split(' ')
	return words
	
def sort_words(words):
	"""Sorts words"""
	return sorted(words)

def print_first(words):
	"""Pops off first word and prints"""
	word = words.pop(0)
	print word
	
def print_last(words):
	"""Pops off last, prints"""
	word = words.pop(-1)
	print word
	
def sort_sentence(sentence):
	"""sorts sentence"""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_last(sentence):
	"""Prints first and last"""
	words = break_words(sentence)
	print_first(words)
	print_last(words)
	
def print_first_last_sorted(sentence):
	"""Sorts and prints first and last"""
	words = sort_sentence(sentence)
	print_first(words)
	print_last(words)