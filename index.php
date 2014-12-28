<?php

// Now, auto compiling a RapydScript to JavaScript if needed before running the web page

// Note:
// The compiling can just as easily be done in the python code,
// but the php code just as accommodating to the 
// maintenance tasks, e.g., compiling rapydscript to js


$source   = 'first.pyj';
//$compiled = 'first.js';	// optional, not used in this version

if ( ! file_exists ($source) ) {
	echo "$source does not exist, exiting."; 
	exit (1); 
}

compile( 'first' ); // or first.pyj


echo system('python front.py 2>&1');	// run web page here, redirecting stderr to stdout useful to debug
	
	
function mod_dt($file) {
	return date ("YmdHis", filemtime($file));
}

function is_compiled($source, $compiled) {
	
	if ( ! file_exists ($source) ) {
		echo "$source file does not exist, exiting";
		return false;
	}
	
	if ( ! file_exists ($compiled) ) {
		echo "$compiled file does not exist" . '<br>';
		return false;
	}
	
	if ( mod_dt($source) >= mod_dt($compiled) )
		return false;
	else
		return true;
}


function compile($source, $compiled = 'default_same_name_as_source') {

	if ( ! contains('.pyj' , lower($source) ) )
		$source = $source . '.pyj';

	if ( $compiled == 'default_same_name_as_source' )
		$compiled = without_file_extension($source) . '.js';
	else if ( ! contains('.js' , lower($compiled) ) )
		$compiled = $compiled . '.js';
	
	if ( is_compiled ($source, $compiled) ) {
		echo 'compiled, yes, already done.';
		return;
	}
	
	if ( file_exists($compiled) )
		unlink ( $compiled );

	$cc  = '"C:\Program Files\nodejs\node.exe" ';                                  // note trailing space
	$cc .= '"C:\Program Files\nodejs\node_modules\rapydscript\bin\rapydscript" ';  // note trailing space
	$cc .= "$source -o $compiled";
	system($cc);                                                                   // compiling here

	if ( ! file_exists($compiled) ) {
		echo "$source has a syntax error due to a failure to compile, exiting";
		exit(1);
	}

	echo 'just auto compiled python rapydscript to javascript';
}

function contains ($needle, $haystack) { return strpos($haystack, $needle) !== false; }
function lower($s) { return strtolower ($s); }
function without_file_extension($s) { return substr($s, 0, strrpos($s, ".")); } // without . and file extension

// footnote: todo, each *.pyj in a directory
?>