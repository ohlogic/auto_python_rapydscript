import sys

def modify_it(file, TW=False):
	with open(file, "r+") as fp:
		s = fp.read()
		fp.seek(0)
		
		if (TW):
			s = s.replace('return <%', 'return training_wheels_bit_slower_to_remove("""')
			s = s.replace('<%', 'print training_wheels_bit_slower_to_remove("""').replace('%>', '""")')
			fp.write( s )
		else:
			s = s.replace('return <%', 'return """')
			fp.write(  s.replace('<%', 'print """' ).replace('%>', '"""') )
		fp.truncate() # unnecessary, except when it is
		
if __name__ == "__main__":  # in the case not transferring data from php, then simply revert to a previous version, commit
	# simply remove or comment out the print statements at your convenience, used just for debugging and testing purposes
	if( not len(sys.argv) >= 2 ):
		print "argument is required, which domain name from the initial, starting PHP"
		sys.exit(1)
	
	print (' Preprocessor ')
	
	if ( sys.argv[1] == '-TW' ):

		if ( len(sys.argv) >= 3 ):
			modify_it( file=sys.argv[2], TW=True )
		else:
			print 'python file is required'
			sys.exit(1)
	else:
		modify_it( file=sys.argv[1] )