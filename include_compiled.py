
def this_is_a_test():

	return utags(training_wheels_bit_slower_to_remove(r"""

This is intented to be included as text, and returned as a string
\\a\\1\\2\\3\\4\\5\\6\\7\\8\\9\\b\\f\\v\\r\\n\\t\\0\\x0B   testing3, expected
<!-- escape characters within include files -->

"""))
def python_using_php_htmlentities(s):

	# unsure, put to file to check, echo later
	# unsure, put echo in front of htmlentities
	
	#list = ['\a', '\1', '\2', '\3', '\4', '\5', '\6', '\7']
	#for item in list:
	#	s = s.replace(item, '\\'+item)
	
	s = s + r'\a\1\2\3\4\5\6\7\8\9\b\f\v\r\n\t\0\x0B'
	
	code_init = r""" echo htmlentities('%s'); """ %  s.replace("'", "\\'")  # quotes mess up format string variables, got to give it a raw string literal
																		# especially that first double quote
																
	#to_write("checking_html_entities_output_php_from_python_help.txt", php (code_init) ) #works! # remove this line, just to check output to file is also wysiwyg
	
	#the only thing to fix is a triple double quote within the string !!! (and the raw string limited escaping too)

	width_here = 200
	height_here = 200	
	code_here = utags(training_wheels_bit_slower_to_remove(r"""
echo ('   """ + str(width_here) + """, """ + str(height_here) + """  ');
"""))

	# returning output from php              return  php ( code_init )          to fix !  
	# + php ( code_here )
	
	#var = php(code_init)  # not using at this version, but works!!! 
	
	# not using the following two lines at this time
	#var = var.replace("&lt;tdq&gt;&lt;double&gt;&quot;&quot;&lt;/double&gt;&quot;&lt;/tdq&gt;", '<tdq><double>""</double>"</tdq>')
	#var = var.replace("&lt;double&gt;&quot;&quot;&lt;/double&gt;&quot;" , '<double>""</double>"')
	
	return s
	#return 'now at the point I want<br>' + s + var
	

	
def source_code():

	#pre_pre_processor.py to address """ """ between quick tags and other small things of a raw string literal
	
	return utags(training_wheels_bit_slower_to_remove(r"""

	'how about this nice person you'
 
&quot;&quot;&quot; hello world, within triple double quotes within python quick tags &quot;&quot;&quot;

	<br>
	hello world, this is the source code included file
	<unicode></unicode>
	
	<p> </p>

"""))



# todo:   python_using_php_htmlentities

def source_code_output(): # good at this point, it return a string
	return utags(training_wheels_bit_slower_to_remove(r"""
	

{**{source_code_htmlentities_form}**}
	

""")).format( source_code_htmlentities_form = python_using_php_htmlentities( source_code() ) )
	
def console_log_function():
	return utags(training_wheels_bit_slower_to_remove(r"""
	
     /**
     * Logs messages/variables/data to browser console from within php
     *
     * @param $name: message to be shown for optional data/vars
     * @param $data: variable (scalar/mixed) arrays/objects, etc to be logged
     * @param $jsEval: whether to apply JS eval() to arrays/objects
     *
     * @return none
     * @author Sarfraz
     */
     function logConsole($name, $data = NULL, $jsEval = FALSE)
     {
          if (! $name) return false;
 
          $isevaled = false;
          $type = ($data || gettype($data)) ? 'Type: ' . gettype($data) : '';
 
          if ($jsEval && (is_array($data) || is_object($data)))
          {
               $data = 'eval(' . preg_replace( '#[\\a\\1\\2\\3\\4\\5\\6\\7\\8\\9\\b\\f\\v\\r\\n\\t\\0\\x0B]+#', '', json_encode($data)) . ')';
               $isevaled = true;
          }
          else
          {
               $data = json_encode($data);
          }
 
          # sanitalize
		  $data = $data ? $data : '';
          $search_array = array("#\\'#", '#\\"\\"#', "#\\'\\'#", "#\\n#", "#\\r\\n#");
          $replace_array = array('"', '', '', '\\\\n', '\\\\n');
          $data = preg_replace($search_array,  $replace_array, $data);
          $data = ltrim(rtrim($data, '"'), '"');
          $data = $isevaled ? $data : ($data[0] === "'") ? $data : "'" . $data . "'";
 
$js = <<<JSCODE
\n<script>
     // fallback - to deal with IE (or browsers that don't have console)
     if (! window.console) console = {};
     console.log = console.log || function(name, data){};
     // end of fallback
 
	// I innovated a start and end tag for hexadecimal content (the tag is of course arbitrary, though seems to fit the purpose (apropos))
    
	function not(s){return !s;}
	
	function hex2asc(pStr) {
	
		if (not( typeof pStr === 'string') )			// alert(typeof pStr);
		return pStr;

		// todo: to check for minimum lengths at this point 

		var startHexTag = pStr.substr(0, 5);			// start tag to indicate hexadecimal content is <hex>

		var endHexTag = pStr.substr(pStr.length - 6); 	// end tag to indicate hexadecimal content is </hex>

		if ( not ( startHexTag === "<hex>" && endHexTag === "</hex>" ) )
		return pStr;

		var data = pStr.substring(5, pStr.length - 6 )

        tempstr = '';
        for (b = 0; b < data.length; b = b + 2) {
            tempstr = tempstr + String.fromCharCode(parseInt(data.substr(b, 2), 16));
        }
        return tempstr;
    }
 
     console.log('$name');
     console.log('------------------------------------------');
     console.log('$type');
     console.log(hex2asc($data));
     console.log('\\\\n');
</script>
JSCODE;
 
          echo $js;
     } # end logConsole
	 
	 
//echo( ' <br> {**{hello}**} <br>');	 

//echo( '{**{howdy}**}');

""")).format (  hello='hello world', howdy='very well thanks' )