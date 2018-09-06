class Song(object):
	
	# essentially class constructor
	# self means it takes its class object as an argument
	def __init__(self, lyrics):
		self.lyrics = lyrics # one member variable
	
	# all functions refer to self 
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued", 
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
						"with pockets full of shells"])
						
three_lions = Song(["It's coming home",
					"It's coming home",
					"It's coming",
					"Football's coming home"])
	
lyrics = ["Beetlebum", "What you done", "She's a gun", "What you done", "Beetlebum"]

beetlebum = Song(lyrics)

beetlebum.sing_me_a_song()
	
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

three_lions.sing_me_a_song()