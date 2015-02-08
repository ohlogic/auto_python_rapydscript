import sys
import re

def print_args(s):
	for item in s:
		print 'ARG:(' + item + ')'

def findindices_of_nonwhitespace(s): # string  , returns tuple  (index and item) , this function not used for now
                                     # split function  enhanced to also return the indices of each item 
	arr = s.split()
	t=[]
	for item in arr:
		i=0
		i = s.find(item, i)
		t.append((i,item))
	return t		

def adjacent(itemA, itemB, new, s): # skips whitespace  # regrettably had to resort to this regex, required, therefore this function
	
	# something like this should be possible (using itemA and itemB)
	restr = itemA + r'\s{0,}' + itemB  # not using this string because,
	# due to the operation of regex and its variability it's due to escaping of characters and other reasons
	
	# therefore:
	return re.sub(r'\(\s{0,}<%', new, s)  # 0 to many spaces in between the ( and <%     #note: i had to escape the open parenthesis in this regex search
	
	
def algorithm(s, tw, uni_val=str(True) ):
	
	uni_str = '.unicode_markup('+uni_val+')'
	
	if (tw):
	
		s = s.replace('return <%', 'return utags(training_wheels_bit_slower_to_remove(r"""')
		s = s.replace('= <%', '= utags(training_wheels_bit_slower_to_remove(r"""')
		
		#just added
		#s = s.replace('( <%', '( utags(training_wheels_bit_slower_to_remove(r"""' ) # specifically for print_wwwlog though turned off print literal feature for now
		# and if smushed
		#s = s.replace('(<%', '( utags(training_wheels_bit_slower_to_remove(r"""' )
		
		# updated the two previous statements with the following improved statement encompassing all cases (of the indented purpose) # 2015.02.07
		s = adjacent('(', '<%', '( utags(training_wheels_bit_slower_to_remove(r"""', s)
		
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