<?php

// Now, auto compiling a RapydScript to JavaScript if needed before running the web page

// Note:
// The compiling can just as easily be done in the python code,
// but the php code just as accommodating to the 
// maintenance tasks, e.g., compiling rapydscript to js


$source   = 'first.pyj';
$compiled = 'first.js';

if (! file_exists ($source)  ) {
	echo "$source does not exist, exiting."; 
	exit (1); 
}


if ( is_compiled ($source, $compiled) )
	echo 'compiled, yes';
else {
	
	if ( file_exists($compiled) )
		unlink ( $compiled );	// delete so any previous versions aren't mistaken 
	                            // as an up to date compiled version that could happen when there
								// is a syntax error in the rapydscript source code
	
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

	
	
	
	// perhaps a final maintenance check that compiled js files exist
	if ( ! file_exists($compiled) ) {
		echo "$source does not exit, exiting";
		exit(1);
	}
	
	
	echo system('python front.py');	// run web page here
	
	
	
function mod_dt($file) {
	return date ("YmdHis", filemtime($file));
}

function is_compiled($source, $compiled) {
	
	if (! file_exists ($source)  ) {
		echo "$source file does not exist, exiting";
		return false;
	}
	
	if (! file_exists ($compiled)  ) {
		echo "$compiled file does not exist" . '<br>';
		return false;
	}
	
	if (mod_dt($source) >= mod_dt($compiled) )
		return false;
	else
		return true;
}

// footnote: todo, can compile a list of *.pyj  or  each *.pyj in a directory
?>