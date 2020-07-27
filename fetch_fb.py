import importlib, traceback
from util import *
from config import *

fetch_data = manager.dict()
time_fetched = manager.dict()

fb_scraper = importlib.import_module('includes.facebook-scraper.facebook_scraper', None)
fb_api = importlib.import_module('includes.facebook-api-crawler.facebook_api_crawler', None)

def fetch_api(fb_api, name, last_time):
	tmp = fb_api.get_posts(name, fbToken, time=str(last_time))
	if (tmp == -1):
		return -1
	for index, post in enumerate(tmp):
		if post["link"] != None and "facebook" in post["link"].split("/")[2]: # Shared posts
			tmp[index]["text"] += "\nShared from: " + post["link"]
	return tmp

def fetch_scraper(fb_scraper, name, last_time):
	if fb_email is None:
		tmp2 = [post for post in fb_scraper.get_posts(name, pages=3)]
	else:
		tmp2 = [post for post in fb_scraper.get_posts(name, pages=3, credentials=(fb_email, fb_pass))]

	tmp = []
	last = False
	for index, post in enumerate(tmp2):
		post["text"] = post["post_text"]
		if post["post_url"] != None:
			post["post_url"] = post["post_url"].replace("m.facebook.com", "facebook.com")
		if post["time"] != None and post["time"] > last_time: # Normal posts
			if post["shared_text"] != "" and post["link"] is None:
				post["text"] += "\n\nShared from: " + post["post_url"]
				post["text"] += "\n" + post["shared_text"]
			elif post["shared_text"] != "" and post["image"] is not None: # Link to external website
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

def process_fb_page(page):
	global fetch_data
	global time_fetched

	try:
		name = page["name"]
		fb_page = page["fb_page"]
		last_time = get_time_file(name)
		
		tmp = -1 #fetch_api(fb_api, fb_page, last_time)
		if (tmp == -1): # Facebook permissions stuff..
			tmp = fetch_scraper(fb_scraper, fb_page, last_time)

		time_fetched[name] = datetime.now()
		
		tmp.reverse()
		fetch_data[name] = tmp

		print("{} end, found {} posts".format(name, len(tmp)))

	except KeyboardInterrupt:
		print("Killed by ctrl+c")
		exit(-1)
	except Exception as e:
		report_exception("Fetching {} from facebook broke".format(name), e)
