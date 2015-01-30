import sys

def print_args(s):
	for item in s:
		print 'ARG:(' + item + ')'

def algorithm(s, tw):
	if (tw):
		s = s.replace('return <%', 'return training_wheels_bit_slower_to_remove("""')
		s = s.replace('= <%', '= training_wheels_bit_slower_to_remove("""')		
		s = s.replace('<%', 'print training_wheels_bit_slower_to_remove("""').replace('%>', '""")')

	else:
		s = s.replace('return <%', 'return """')
		s = s.replace('= <%', '= """')		
		s = s.replace('<%', 'print """' ).replace('%>', '"""')
	return s

def modify_it(file, TW=False):
	with open(file, "r+") as fp:
		s = fp.read()
		fp.seek(0)
		
		if (TW):
			fp.write( algorithm(s,TW) )
		else:
			fp.write( algorithm(s,TW) )
		fp.truncate() # unnecessary, except when it is

def modify_diff(source, TW=False, dest=''):
	with open(source, 'r') as rp:
		s = rp.read()
	
	with open(dest, 'w') as wp:
		if (TW):
			wp.write( algorithm(s,TW) )
		else:
			wp.write( algorithm(s,TW) )
		
if __name__ == "__main__":  # in the case not transferring data from php, then simply revert to a previous version, commit
	# simply remove or comment out the print statements at your convenience, used just for debugging and testing purposes
	if( not len(sys.argv) >= 2 ):
		print "argument is required, which domain name from the initial, starting PHP"
		sys.exit(1)
	
	print (' Preprocessor ')
	print_args(sys.argv)
	
	if ( sys.argv[1] == '-TW' ):

		if ( len(sys.argv) == 3 ):
			modify_it( file=sys.argv[2], TW=True )
		elif( len(sys.argv) == 4):
			modify_diff( source=sys.argv[2], TW=True, dest=sys.argv[3])
		else:
			print 'python file is required'
			sys.exit(1)
	else:
		modify_it( file=sys.argv[1] )