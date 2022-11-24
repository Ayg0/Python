from sys import argv

if len(argv) == 2:
	if (argv[1].startswith(tuple(['+', '-'])) and argv[1][1:].isdigit()) or argv[1].isdigit():
		i = int(argv[1])
		print("I'm " + ("odd" if i % 2 == 1 else "a zero" if i == 0 else "even"))
	else:
		print("Error, argument is not an integer")