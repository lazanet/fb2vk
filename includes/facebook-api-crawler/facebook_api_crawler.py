import json, sys, requests, re
from datetime import datetime
from .util import *

def get_posts(pageID, fbToken, time = str(datetime.now())):
	baseUrl = "https://graph.facebook.com/v3.0/"
	try:
		options = { "access_token":fbToken, "fields":"id,message,created_time,full_picture,link,type,permalink_url", "since":time, "limit":50 }
		wall = curl_get(baseUrl + "{}/posts".format(pageID), options)
		wall = json.loads(wall)

		data = []
		i = 1
		for wall_post in wall["data"]:
			post = {}
			post["post_id"] = wall_post["id"].split("_")[1]
			post["time"] = fbTime2normal(wall_post["created_time"])
			post["post_url"] = wall_post["permalink_url"]

			if "message" in wall_post:
				post["text"] = wall_post["message"]

			if "link" in wall_post:
				post["link"] = wall_post["link"] 

			if wall_post["type"] == "photo":
				post["image"] = wall_post["full_picture"]
				del post["link"]

			data.append(post)

			print( "{} out of {}".format( i, len(wall["data"])) )
			i += 1
		return data

	except Exception as e:
		#print(e) 
		return -1


def fbTime2normal(t):
	tmp = datetime.strptime(t.replace(" ",""),'%Y-%m-%dT%H:%M:%S+0000')
	return tmp
