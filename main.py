import importlib
from config import *
from util import *
from pprint import pprint, pformat
from datetime import datetime

fb_scraper = importlib.import_module('includes.facebook-scraper.facebook_scraper', None)
fb_api = importlib.import_module('includes.facebook-api-crawler.facebook_api_crawler', None)
vk = importlib.import_module('includes.vkontakte-poster.vkontakte_poster', None)

def fetchAPI(fb_api, name, lastTime):
	tmp = fb_api.get_posts(name, fbToken, time=str(lastTime))
	if (tmp == -1):
		return -1
	for index, post in enumerate(tmp):
		if post["link"] != None and "facebook" in post["link"].split("/")[2]: # Shared posts
			tmp[index]["text"] += "\nShared from: " + post["link"]
	return tmp

def fetchScraper(fb_scraper, name, lastTime):
	tmp2 = [post for post in fb_scraper.get_posts(name, pages=3)]
	tmp = []
	last = False
	for index, post in enumerate(tmp2):
		if post["post_url"] != None:
			post["post_url"] = post["post_url"].replace("m.facebook.com", "facebook.com")
		if post["time"] != None and post["time"] > lastTime: # Normal posts
			if post["shared_text"] is not "" and post["link"] is None:
				post["text"] += "\n\nShared from: " + post["post_url"]
				post["text"] += "\n" + post["shared_text"]
			elif post["shared_text"] is not "" and post["image"] is not None: # Link to external website
				post["image"] = None # Don't want to upload preview as image
			del post["shared_text"]
			tmp.append(post)
			last = True
		elif post["time"] == None and last: # Shared posts...
			if tmp[-1]["text"] == None:
				tmp[-1]["text"] = ""
			tmp[-1]["link"] = post["post_url"]
			last = False
		else:
			last = False
		
	return tmp

######################################################################
# Main program
######################################################################

fetchData = {}
timeFetched = {}

print("Bot started")
print()
print("Fetching facebook data...")

for page in data:
	name = page["name"]
	fbPage = page["fbPage"]
	lastTime = getTimeFile(name)
	
	tmp = -1#fetchAPI(fb_api, fbPage, lastTime)
	if (tmp == -1): # Facebook permission stuff..
		tmp = fetchScraper(fb_scraper, fbPage, lastTime)

	timeFetched[name] = datetime.now()
	
	tmp.reverse()
	fetchData[name] = tmp

	print(name + " end, found {} posts".format(len(tmp))) 	

print()
print("Facebook data downloaded!")
print()

print()
print("Posting data to vKontakte...")
print()

for page in data:
	name = page["name"]
	posts = fetchData[page["name"]]
	vkPageId = page["vkPageId"]
	userToken = page["userToken"]	
	status = 0

	print("Page: " + name)
	for post in posts:
		message = post["text"]
		image_url = post["image"]
		link = post["link"]

		status = vk.post(vkPageId, userToken, message, image_url, link)
		if status != 0:
			break

	if status == 0:
		saveTimeFile(name, timeFetched[name])
	
	print(name + " done!")
	print()

print("Data posted! End.")
