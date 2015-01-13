auto_python_rapydscript
=======================

The purpose is automatic compiling of python like Rapydscript to JavaScript for client side; 
in addition to a web page written in python, output through minimal php code using the php module

Requirements:

node.exe   (to compile rapydscript)

python.exe (to use a python script for server side web page creation, 
			optional perhaps but nice to have python server side 
			and (python like) client side with rapydscript)

RapydScript note:

*.pyj files are edited by the user.

*.js  files are auto generated and should not be manually edited.

Also note:

The RapydScript simple example provided displays its output 
through the browser's console log, Firebug's console log, etc.


2015-01-13
Added the feature of python tags, open and close <%  %> for triple quoted strings with a few format text replacements 
to deal with curly brackets within triple quoted strings when used together with the format function.