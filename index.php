<?php

// Now, auto compiling a RapydScript to JavaScript if needed before running the web page

// Note:
// The compiling can just as easily be done in the python code,
// but the php code just as accommodating to the 
// maintenance tasks, e.g., compiling rapydscript to js


// Just revert to previous version, commit 
// if not using a same domain name with different domain suffixes, e.g., domain.com, domain.net
// Though the idea if needed is to eventually transfer data to the python code, if only a few arguments
// simply through a list of parameter/arguments, with more, then to use json via a php array encode and send that

echo domain_name_endswith() . '<br>'; // goes to py code

function domain_name_endswith() {	  // or contains, domain_suffix, etc.    // or just argument to py code

$ret1 = 'A';    // plan
$ret2 = 'WIDE'; // B
	if(isset($_SERVER['SERVER_NAME']) ) {
		$s = $_SERVER['SERVER_NAME'];
	//  :D  Lee
		$s = right(raise($s), 2);
		if ($s == 'US')
			return $ret1;  // or boolean type
		else
			return $ret2;  // world, earth, whatever, the language thing issue...
	}
return $ret1;
}


$source   = 'first.pyj';
//$compiled = 'first.js';	// optional, not used in this version

if ( ! file_exists ($source) ) {
	echo "$source does not exist, exiting."; 
	exit (1); 
}

compile( 'first' ); // or first.pyj

/* Note: New Feature   --   Open and Close Tags for ONLY the  .py  file  ( not the RapydScript code file )
  
   In this version I add the php feature to python of  open and close  tags that define 
   the beginning of python code and when the end of the python code occurs that are the tags   <%   and   %>
   exactly the way   <?php   and   ?>   work in PHP.
   
   This happens in the simple preprocessor step, it also gives an optional switch to enable a bit simpler python coding,
   and then the statement after the double ampersand.
*/
# the double ampersand executes only if the first command is successful (the preprocessor step)
echo system('python simple_preprocessor.py -TW front.py && python front.py '.domain_name_endswith().' 2>&1');	// run web page here, redirecting stderr to stdout useful to debug
	
	
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
function raise($s) { return strtoupper ($s); }
function without_file_extension($s) { return substr($s, 0, strrpos($s, ".")); } // without . and file extension
function left($str, $length)  {return substr($str, 0, $length);}
function right($str, $length) {return substr($str, -$length);  }
// footnote: todo, each *.pyj in a directory
?>