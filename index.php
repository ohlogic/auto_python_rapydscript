<?php
	// Simply call the python script to create the web page
	// within the python script, the includes of css, rapydscript created javascript,
	// and other javascript libraries may occur.
	//
	// Optionally, php could further process the page, for now, 
	// python processing the page is fine.
	
	echo system('python front.py');
?>