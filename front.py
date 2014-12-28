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

# test example, don't forget to have php.exe and php5ts.dll in PATH
width = 100
height = 100	
code = """
echo ('   """ + str(width) + """, """ + str(height) + """  ');
"""

	
# Note, any JavaScript or any other code that contains a curly brace 
# must double the curly brace when using the python format function with the triple double-quoted string, 
# but not in a JavaScript src file (regardless of using the format function or not)
print """

<!DOCTYPE html>
<html lang="en">
<head>
<title></title>
<link rel="stylesheet" type="text/css" href="css/page_frame.css" />
<script src="first.js"></script>

</head>
<body>

<div id="container">

<div id="top">{top_content}</div>

<div id="mid">{mid_content}</div>

<div id="end">{end_content}</div>

</div>

PHP test: {php_test}
</body>
</html>

""".format (  
	# variables used
	top_content = top_content(),
	mid_content = mid_content(),
	end_content = end_content(),
	php_test    = php(code)  # just testing, remove if coding anything serious
)
