import json
import requests

print "Connecting..."

r = requests.get('https://api.particle.io/v1/events/wire_state?access_token=61d3643c20fc05c2cdc5c42f3d0e80d6b56638e5', stream=True)

print "Connected."

for line in r.iter_lines(1):
	if not line.startswith('data: '):
		continue
	line = line[6:]
	event = json.loads(line)
	print event['data']
	

