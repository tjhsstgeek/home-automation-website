#!/usr/bin/python

import pyhue
import sys
import cgi


print "Content-Type: text/html\n\r"
print "\n\r"

form = cgi.FieldStorage()
lightstate = form.getvalue("onoff")
print lightstate

bridge = pyhue.Bridge("192.168.0.10","fkEGsDaVfOk745iChwLTQlMNYpAE8uhN2Nb-diMP")
for light in bridge.lights:
	if lightstate == "false":
		light.on = False
	if lightstate == "true":
		light.on = True
		
print "<a href='/'> home </a>"
