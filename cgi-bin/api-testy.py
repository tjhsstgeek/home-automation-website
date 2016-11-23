#!/usr/bin/python

import json
import os
import requests
import time

from pprint import pprint
from urllib2 import urlopen, URLError

base_url = 'https://api.particle.io/v1'
device_id = '23002e000a51353335323535'
var_name = 'samtest'
access_token = '61d3643c20fc05c2cdc5c42f3d0e80d6b56638e5'
get_var_url = '%s/devices/%s/%s?access_token=%s' % (
		base_url, device_id, var_name, access_token)

response = json.loads(requests.get(get_var_url).content)

# Whether the wires are touching or not.
sense_value = response['result']

print 'Content-type: application/json'
print
print json.dumps({'sense_valbue': sense_value})
