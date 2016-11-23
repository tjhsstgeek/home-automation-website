############ 0. INITIALIZE AND IMPORT ############

#/usr/bin/python


# Access Token: 61d3643c20fc05c2cdc5c42f3d0e80d6b56638e5
# Device ID: 23002e000a51353335323535

import json
import os
import time
import requests
from urllib2 import urlopen, URLError
from pprint import pprint







############ 1. PARAMS ############
IMG_NUM = 5
upl_req_url = 'https://api.pushbullet.com/v2/upload-request'
push_url = 'https://api.pushbullet.com/v2/pushes'
get_var_url = 'https://api.particle.io/v1/devices/23002e000a51353335323535/wire_state?access_token=61d3643c20fc05c2cdc5c42f3d0e80d6b56638e5'
wait_event_url = ''
# download_url = 'http://68.33.1.197:8080/photo.jpg'
# download_url = 'http://192.168.0.27:8080/photo.jpg'

headers ={
	"Authorization": "Bearer o.BjmlDfXlAN6ncJswRY26Hdvr7xQG4uiV",
	"Content-Type": "application/json"
}

upl_req_data ={
	"file_name": "photo.jpg",
	"file_type": "image/jpeg"
}



############ 2. WAIT FOR HARDWARE INTERRUPT ############
AshlieFace = 0

print "Waiting for hardware interrupt....."
while (AshlieFace == 0):
	u = requests.get(get_var_url)
	print "requests.get(): " + u
	r = u.content
	print "requests.get().content: " + r
	var_resp = json.loads(r)

	AshlieFace = var_resp['result']
	
	


print AshlieFace
print "Interrupt received."


############ 3. LOOP ############

count = 0
while (count < IMG_NUM):

	############ 2a. DOWNLOAD IMAGE ############
	download_url='http://placekitten.com/200/'+str(count+200)
	pho_name = 'photo'+str(count)+'.jpg'
	print "Downloading image " + pho_name + "..."
	img_cur = urlopen(download_url).read()
	a_file = open(pho_name, 'w')
	a_file.write(img_cur)
	a_file.close()
	print "Finished."
	
	count = count + 1

	
	
count = 0
while (count < IMG_NUM):
	############ 3b. NEW UPLOAD REQUEST & PARSE JSON ############
	print "Requesting new upload..."
	u = requests.post(upl_req_url, data=json.dumps(upl_req_data), headers=headers)
	r = u.content
	upl_req_resp = json.loads(r)
	
	upl_url = upl_req_resp['upload_url']		# upload file to here
	file_url = upl_req_resp['file_url']		# file will be located here
	
	print "Acquired."




	############ 3c. JSON FILES OBJECT & UPLOAD ############
	pho_name = 'photo'+str(count)+'.jpg'
	files = {
        	'file': open(pho_name,'r'),
        	'filename':'photo.jpg'
	}

	print "Uploading..."
	upl_resp = requests.post(upl_url, files=files)

	############ 3d. CREATE PUSH REQUEST ############
	push_text = 'Image: ' + str(count+1)

	push_data = {
		"file_name":"photo.jpg",
		"file_url":file_url,
		"type":"file",
		"title":"Motion Detected",
		"body":push_text,
		"channel_tag":"testderp"
	}
	print "Done."
	
	
	
	print "Pushing image " + str(count+1) + "..."
	push_resp = requests.post(push_url, data=json.dumps(push_data), headers=headers)
	print "Pushed."
	############ 3e. ITERATE ############
	count = count + 1
	
