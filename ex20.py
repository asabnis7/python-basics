from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)

def print_line(line_ct, f):
	print line_ct, f.readline()
	
current_file = open(input_file)

print "Full file"
print_all(current_file)

print "Rewind"
rewind(current_file)

print "Three lines"

current_line = 1
print_line(current_line, current_file)
current_line += 1
print_line(current_line, current_file)
current_line += 1
print_line(current_line, current_file)