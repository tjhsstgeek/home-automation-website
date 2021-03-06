#!/usr/bin/python

import json
import os
import requests
import time

from pprint import pprint
from urllib2 import urlopen, URLError

base_url = 'https://api.particle.io/v1'


wire_device_id = '23002e000a51353335323535'
furnace_device_id = 'garbage value from KESH'


# dictionary
target_map = {
	'samtest':		wire_device_id,
	'furnace_val':		furnace_device_id,
	'other_furnace_val':	furnace_device_id
}

# checks that target is a field in target_map
if target not in target_map:
	# throw a big fat 403 here
	print 'STATUS: 403 FORBIDDEN'
	print
	print 'FORBIDDEN'
	os.exit(1) # error occured

access_token = '61d3643c20fc05c2cdc5c42f3d0e80d6b56638e5'


device_id = target_map[target]
get_var_url = '%s/devices/%s/%s?access_token=%s' % (
		base_url, device_id, target, access_token)

response = json.loads(requests.get(get_var_url).content)

# Whether the wires are touching or not.
value = response['result']

	


print 'Content-type: application/json'
print
print json.dumps({'value': value})
