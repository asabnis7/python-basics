def cheese_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d crackers!" % boxes_of_crackers
	
print "Give individual numbers"
cheese_crackers(20,30)

print "Use script variables"
amount_cheese = 15
amount_crackers = 20

cheese_crackers(amount_cheese, amount_crackers)

print "Do math inside"
cheese_crackers(5+23/2, 6*4)

print "Combine variables and math"
cheese_crackers(amount_cheese+4, amount_crackers*7)