import os
import sys
from subprocess import PIPE, Popen, STDOUT
import time

same_file = False	# is True or False , gets value from PHP (global or make App class due to 
														 # global variables frowned upon, i.e., not best practices)
														 # began to import from PHP, still a todo, at this time
PRINTOUT = False	# for print statements used by print_test() to review variables, etc. perhaps a form of browser console logging is the way to go
					# https://sarfraznawaz.wordpress.com/2012/01/05/outputting-php-to-browser-console/
					# this todo: done 2015.01.28
def mod_dt(file):
	return time.strftime("%Y%m%d%H%M%S",time.localtime(os.path.getmtime(file)));
	
def to_write(file, s):
	with open(file, 'w') as fp:
		fp.write(s)					
					
def print_test(s):
	global PRINTOUT
	if (PRINTOUT):
		print s
		
def exists(path):
	return True if ( os.path.isfile(path) or os.path.isdir(path)) else False

def file_exists(path):
	return os.path.isfile(path)
	
def is_compiled(source, dest):

	if not file_exists(dest): # exists def nice, file_exists works fine too
		return False

	if ( mod_dt(source) >= mod_dt(dest) ):
		return False
	else:
		return True
		
def compile_include_quick_tags(file):
	global same_file
	
	if(not same_file):
		compiled = file[:-3] + '_compiled.py'
	else:
		compiled = file
	
	if ( is_compiled(file, compiled) ): # working on
		print '(INCLUDE ALREADY COMPILED)'
		return compiled                                   #
	
	print '(INCLUDE NOT compiled yet, therefore COMPILING)'
	
	os.system('"python.exe simple_preprocessor.py -TW '+file+' '+compiled+'  2>&1"')
	
	print_test( 'INCLUDING THIS FILE(' + compiled + ')' )
	return compiled # run pre_processor on it, with file being the source and  it as the dest
		
	# any includes done here to evaluate one file format variable, Q. can I include in a def,function
	
	
def include_quick_tags_file(source):
	global same_file
	
	print_test( 'POINT #1 file is:('+ source + ')' )
	f = os.path.abspath(compile_include_quick_tags(source)) # compiled variable
	print_test( '<br>file to include('+f+')' )
	
		# initially the idea was to compile here with the following statement:
		#execfile(compiled) # require fullpath, includes file   (though having a scope issue here)
				
	#if (same_file):
		# need to postprocessor.py the file after compiling
		# due to the way execfile currently works, cannot call from a def,function as I intend it to work (simply include)
	
	return f # hmm, how in -antastic is this, workaround needed by the receiver of this return when same file format is true


def execfile_fix(file): # workaround, due to execfile not working (as i'd like it to work (as expected)) from within a def,function
	global same_file
	
	if(same_file):
		os.system('"python.exe simple_postprocessor.py -TW '+file+' 2>&1"');


		
# INCLUDES TO BE PLACED HERE

file_to_include = 'include.py'
# including this way due to execfile does not including a file within a def,function as I expected
#execfile(include_quick_tags_file(file_to_include))	# this functin used to include each python file with quick tags		 


# NOTE: include section of source code with two entries due to workaround needed for execfile def,function
execfile(include_quick_tags_file(file_to_include))
execfile_fix(file_to_include) # when same file format is used, post_procesor.py (not used when using different file format)
							  # NOTE: fix does not need to be removed if using different file format (due to boolean check)
							  # otherwise, workaround is to convert after output() def called from main, with list of include files to convert back

							  					  
def print_args(s, intro=''):
	print_test( intro )
	for item in s:
		print_test( 'ARG:(' + item + ')' )
		

def create_superglobals(args):
	global same_file
	# idea to transfer superglobals from PHP here
	
               # experimental, just testing PHP called within Python
def php(code): # shell execute PHP from Python (that is being called from php5_module in Apache), for fun...
	p = Popen(['php'], stdout=PIPE, stdin=PIPE, stderr=STDOUT) # open process
	o = p.communicate('<?php '+ code +'\n ?>')[0]
	try:
		os.kill(p.pid, signal.SIGTERM)	# kill process
	except:
		pass
	return o

def top_content():
	return 'header'
	
def mid_content():
	return <%
	
This is a test, <br>it is actually within a triple double quoted string

%>
	
def end_content():
	return 'footer'
	
# in the case not transferring data from php using multiple domains, simply revert to a previous version, commit 
def domain_name(s):   
	if(s == 'A'):
		return 'us'
	elif(s == 'WIDE'):
		return 'com'
		
def training_wheels_bit_slower_to_remove(s): # recommend: to remove this function for production code and edit code as required
                                             # just chose an arbitrary tag to represent the python format variables, works nicely, for now
	return s.replace('{', '{{').replace('}', '}}').replace('{{**{{', '{').replace('}}**}}', '}')

# test example, don't forget to have php.exe and php5ts.dll in PATH
width = 100
height = 100	
code = """
echo ('   """ + str(width) + """, """ + str(height) + """  ');
"""

# Note, any JavaScript or any other code that contains a curly brace 
# must double the curly brace when using the python format function with the triple double-quoted string, 
# but not in a JavaScript src file (regardless of using the format function or not).

# It further verifies that the compiled Python-like RapydScript JavaScript will indeed run,
# with the use of jQuery's .ready and .getScript that also verifies the JavaScript is syntactically correct.
# If it is correct to the browser's JavaScript engine, the console.log will successfully print to the browser's console.

def output(name):
# With this New Feature: Open and Close Tags for this Python file 
# (It allows syntax highlighting within the tags, and eases coding)
# Note that the following opening tag, (less-than sign and percent sign) will be replaced by the simple_preprocessor.py
# with this:  PRINT training_wheels_bit_slower_to_remove(""" (lowercase) NOTE: this exact comment line obviously does not run.
	<%

<!DOCTYPE html>
<html lang="en">
<head>
<title></title>
<script src="js/jquery-1.11.2.min.js"></script>
<link rel="stylesheet" type="text/css" href="css/page_frame_{**{domain}**}.css" />
<script src="first.js"></script>

<script>
$(document).ready(function() {
	console.log('jquery 1.11.2 initialized');
	console.log('app.js loading...  if capitalized done. statement does not appear next, or as the print line to the console, there is an error occurring');
});

jQuery.getScript("first.js", function() {
	console.log('DONE.');
});
</script>

</head>
<body>
<br>{**{testing_output}**}<br>
<div id="container">

<div id="top">{**{top_content}**}</div>

<div id="mid">{**{mid_content}**}</div>

<div id="end">{**{end_content}**}</div>

</div>

PHP test: {**{php_test}**}
</body>
</html>

%>.format (  
	# variables used
	top_content = top_content(),
	mid_content = mid_content(),
	end_content = end_content(),
	php_test    = php(code),  # just testing, remove if coding anything serious
	
	domain      = domain_name(name), # or something like whether a mobile device,
                                     # resolution information, etc. to select which css that fits	

testing_output = this_is_a_test()    # test of include file using quick tags python syntax
)

	# testing writing print statement to the web browser 
	# the intent is to create a python function to wrap the writing with print statements to the web browser's console
	code_init = """
$name = 'Stan';
 
$fruits = array("banana", "apple", "strawberry", "pineaple");
 
$user = new stdClass;
$user->name = "Switaj";
$user->desig = "CEO";
$user->lang = "PHP Running Through subprocess (Python)";
$user->purpose = "To print log messages to the browser console messages to the browser";
 var_dump($fruits);
logConsole('$name var', $name, true);
logConsole('An array of fruits', $fruits, true);
logConsole('$user object', $user, true);
"""


	# written to print to the console log of a web browser
	# had to use decode string escape before being able to replace problematic characters as listed
	# assigned arbitrary variables to replace in the function that returns a string also demonstrating
	# the feature of including an external python file that uses quick tags, (both open and close tags), and a format string variable syntax of {**{variable_name}**}
	s = (code_init + "\n" + console_log_function())
	s = s.replace('{{', '{').replace('}}', '}').replace("#'#", '"').decode('string_escape').replace('HERE', '\\s\\r\\n\\t\\0\\x0B' )
	s = s.replace('a1', "#'#").replace('a2', '#""#').replace('a3', "#''#").replace('a4', "#\\n#").replace('a5', "#\\r\\n#")
	s = s.replace('b4', "\\\\n").replace('b5', "\\\\n").replace('c1', "\\\\n")
	
	to_write('testit.txt', s) # uses to determine problematic characters only, can be removed
	
	print php(  s   )


# ALSO NOTE: On the line immediately starting with the (percent sign and greater-than sign), this is the closing tag
# gets replaced back to (triple double quotes and open parenthesis).

if __name__ == "__main__":  # in the case not transferring data from php, then simply revert to a previous version, commit
	create_superglobals(sys.argv)
	print_args(sys.argv, '<br>HERE front.py '+'<br>')
	
	if( not len(sys.argv) >= 3 ):
		print "argument is required, which domain name from the initial, starting PHP"
		print "argument required, same file format bool"
		sys.exit(1)
		
	output(sys.argv[1])