
# Euclid's Algorithm for finding GCD
def euc (a, b):
	if a % b == 0:
		print "GCD: %d" % b
	else:
		euc(b, a % b)