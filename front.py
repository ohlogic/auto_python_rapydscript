def top_content():
	return 'header'
	
def mid_content():
	return 'middle'
	
def end_content():
	return 'footer'
	
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

</body>
</html>

""".format (  
	# variables used
	top_content = top_content(),
	mid_content = mid_content(),
	end_content = end_content()
)