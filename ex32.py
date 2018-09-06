count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

# first loop goes through a list

for number in count:
	print "This is count %d" % number

for fruit in fruits:
	print "A fruit of type %s" % fruit

for i in change:
	print "I got %r" % i
	
elements = []
elements = range(0,6)
# for i in range(0,6):
	# print "Adding %d to the list" % i
	# # append is understood by lists
	# elements.append(i)
	
for i in elements:
	print "Element is %d" % i
	

nums = [[1,2,3],[4,5,6]]
rows = 2
columns = 3
for i in range(0,rows):
	for j in range(0,columns):
		print "Element is: %d" % (nums[i][j])