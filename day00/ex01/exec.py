import sys


if len(sys.argv) != 1:
    print(((' '.join((sys.argv[1:])))[::-1]).swapcase())
else:
    print("string as argument, reverses it, swaps its letters case and print the result")
