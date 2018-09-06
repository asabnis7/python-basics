from sys import exit
from random import random

def penalty():
	print """
	It's a penalty!
	Which way do you shoot?
	Straight, right or left?
	"""
	
	shot = raw_input("> ")
	hit = random()*5 + 1
	
	if good_luck == True:
		print "Nothing can stop you now!"
		win()
	elif good_luck == False:
		if (shot == "left") and (hit < 2.5):
			print "The keeper's saved it!"
			loss()
		elif (shot == "left") and (hit >= 2.5):
			print "The keeper gets a hand but it's in!"
			win()
		elif (shot == "right") and (hit < 2):
			print "The keeper goes the wrong way!"
			win()
		elif (shot == "right") and (hit >= 2):
			print "Whoops! He's skied it!"
			loss()
		elif (shot == "straight") and (hit < 3):
			print "The keeper isn't fooled!"
			loss()
		elif (shot == "straight") and (hit >=3):
			print "Wow! Straight through the keeper!"
			win()
		else:
			print "There's no time to lose!"
			penalty()
	else:
		print "Whoops"
		exit(0)


def box():
	print"""
	You have reached the 18-yard box.
	The keeper starts rushing out towards you.
	What do you do?
	
	1. Square the ball.
	2. Chip the keeper. 
	3. Try and curl it around him.
	4. Try and run past him.
	
	Enter a number to continue.
	"""
	move = int(raw_input("> "))
	
	if move == 1:
		print "Your teammate receives the ball but is tackled expertly from behind!"
		loss()
	elif move == 2:
		print "The ball sails over the hapless keeper."
		win()
	elif move == 3:
		print "The keeper is too close and gets a strong hand to it."
		loss()
	elif move == 4:
		print "The keeper fouls you as you go through him!"
		penalty()
		

def midfield():
	
	if good_luck == True:
		print "Hey, you're feeling pretty lucky."
	
	print """
	Kickoff! What do you do?
	
	1. Attempt a wild shot.
	2. Dribble through the team.
	3. Play a slick passing move.
	
	Enter a number to continue.
	"""
	
	center = int(raw_input("> "))
	
	if (good_luck == True):
		if center == 1:
			print "Your shot's caught the keeper off guard!"
			win()
		else:
			print "You've got to the box!"
			box()
	elif good_luck == False:
		if center == 1:
			print "No way you thought that was going to work."
			loss()
		elif center == 2:
			print "You're easily dispossed by the CDM."
			loss()
		elif center == 3:
			print "You carve through the team with ease!"
			box()
		else:
			print "You've got no time to waste!"
			midfield()
	else:
		print "Whoops"
		exit(0)
	
	
def kickoff():
	print"""
	The score is 2-2. 90th minute. 1 minute of injury time remains.
	The league is on the line. You need a win.
	The ref is about to begin.
	"""
	for i in range(5,1):
		print i
	
	midfield()
	
	
def loss():
	print "Oh no! The chance goes begging. Better luck next time."
	exit(0)

def win():
	print "It's a goal and it's a winner!"
	print "The whistle goes. You've done it! Well done."
	exit(0)

def luck():
	prob = random()
	print "Luck:", prob
	if prob >= 0.6 and prob <= 1.0:
		good_luck = True
	else:
		good_luck = False

	return good_luck
	
good_luck = luck() 	
kickoff()