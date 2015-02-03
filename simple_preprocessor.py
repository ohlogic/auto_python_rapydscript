import sys

def print_args(s):
	for item in s:
		print 'ARG:(' + item + ')'

def algorithm(s, tw, uni_val=str(True) ):
	
	uni_str = '.unicode_markup('+uni_val+')'
	
	if (tw):
	
		s = s.replace('return <%', 'return utags(training_wheels_bit_slower_to_remove(r"""')
		s = s.replace('= <%', '= utags(training_wheels_bit_slower_to_remove(r"""')		
		s = s.replace('<%', 'print utags(training_wheels_bit_slower_to_remove(r"""')
#		s = s.replace('%%>', ')'+uni_str )                                    # to remove quick workaround, remove this line
		s = s.replace('%>','"""))')
		
		
#		s = s.replace('""")).format (     %:)>', '""").format (   #  %:)> ')  # to remove quick workaround, remove this line, way to rid one close parenthesis, with the happy face keyword created for this purpose , it comments out the keyword %:)> 
		# statements on line #16 and #20 uncomment to remove unicode type quick python tags i.e., <unicode> </unicode>  though the contents in between the tags remain intact
	else:
		s = s.replace('return <%', 'return utags(r"""')
		s = s.replace('= <%', '= utags(r"""')		
		s = s.replace('<%', 'print utags(r"""' ).replace('%>', '""")')		
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

def modify_diff(source, TW=False, dest='', uni_val=''):
	with open(source, 'r') as rp:
		s = rp.read()
	
	with open(dest, 'w') as wp:
		if (TW):
			wp.write( algorithm(s,TW, uni_val) )
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
		elif( len(sys.argv) == 5):
			modify_diff( source=sys.argv[2], TW=True, dest=sys.argv[3], uni_val=sys.argv[4] )
		else:
			print 'python file is required'
			sys.exit(1)
	else:
		modify_it( file=sys.argv[1] )