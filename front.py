from subprocess import PIPE, Popen, STDOUT
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
	return 'middle'
	
def end_content():
	return 'footer'

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

print training_wheels_bit_slower_to_remove("""

<!DOCTYPE html>
<html lang="en">
<head>
<title></title>
<script src="js/jquery-1.11.2.min.js"></script>
<link rel="stylesheet" type="text/css" href="css/page_frame.css" />
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

<div id="container">

<div id="top">{**{top_content}**}</div>

<div id="mid">{**{mid_content}**}</div>

<div id="end">{**{end_content}**}</div>

</div>

PHP test: {**{php_test}**}
</body>
</html>

""").format (  
	# variables used
	top_content = top_content(),
	mid_content = mid_content(),
	end_content = end_content(),
	php_test    = php(code)  # just testing, remove if coding anything serious
)
