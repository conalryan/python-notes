import sys

def hello(who):
	if (who):
		print('hello {}'.format(who))

l = len(sys.argv)
if l > 1:
 	hello(sys.argv[1])
