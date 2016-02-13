import urllib2
import re

name = "data-name=.*?\"(.+?)\" data-protected"
html_content = urllib2.urlopen('https://twitter.com/Highoff_Bseball').read()

matches = re.findall(name, html_content);

print matches[0];

if len(matches) == 0: 
   print 'I did not find anything'
else:
   print 'My string is in the html'