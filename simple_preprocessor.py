import sys

def read_it(file, TW=False):
	with open(file, "r+") as fp:
		s = fp.read()
		fp.seek(0)
		
		if (TW):
			fp.write( s.replace('<%', 'print training_wheels_bit_slower_to_remove("""').replace('%>', '""")') )
		else:
			fp.write( s.replace('<%', 'print """').replace('%>', '"""') )
			
if __name__ == "__main__":  # in the case not transferring data from php, then simply revert to a previous version, commit

	if( not len(sys.argv) >= 2 ):
		print "argument is required, which domain name from the initial, starting PHP"
		sys.exit(1)
	
	if ( sys.argv[1] == '-TW' ):
		print 'yes, got the TW switch argument'
		
		if ( len(sys.argv) >= 3 ):
			print 'yes, got the file argument'
			read_it( file=sys.argv[2], TW=True )
		else:
			print 'python file is required'
			sys.exit(1)
	else:
		read_it( file=sys.argv[1] )