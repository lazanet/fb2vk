#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from config import *
from util import *
from fetch_fb import *
from time import sleep

vk = importlib.import_module('includes.vkontakte-poster.vkontakte_poster', None)

######################################################################
# Main program
######################################################################
if __name__ == "__main__":
	info("Bot started")
	info("Fetching facebook data...")

	if parallel:
		with Pool(processes=3) as pool: 
			pool.map(process_fb_page, data)	
	else:
		for page in data:
			process_fb_page(page)
	
	info("Facebook data downloaded!")

	info("Posting data to vKontakte...")

	for page in data:
		name = page["name"]
		if name not in fetch_data:
			continue
		posts = fetch_data[page["name"]]
		vk_page_id = page["vk_page_id"]
		user_token = page["user_token"]	
		status = 0

		print("Page: " + name)
		for post in posts:
			message = post["text"]
			image_url = post["image"]
			link = post["link"]

			try:
				vk.post(vk_page_id, user_token, message, image_url, link)
			except Exception as e:
				report_exception("VK posting broke", e)
				status = -1
				break
			sleep(1)

		if status == 0:
			save_time_file(name, time_fetched[name])
		else:
			break
		
		print(name + " done!")
		print()

	report_error_end(vk)
	info("Data posted! End.")
