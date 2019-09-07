import json, sys, requests
from .util import *

def post(pageID, userToken, message=None, image=None, link=None):
	apiVersion = 5.71
	options = {
		"v" : apiVersion,
		"access_token" : userToken,
		"owner_id" : -int(pageID),
		"from_group" : 1 
	}
	
	if message != None:
		options["message"] = message

	if image != None:
		try:
			img = {'photo': ( 'image.jpg', curl_fetch_binary(image) )}
			method_url = 'https://api.vk.com/method/photos.getWallUploadServer?'
			data = { "v" : apiVersion, "access_token": userToken, "gid":int(pageID) }

			response = requests.post(method_url, data, verify=False)
			result = json.loads(response.text)
			upload_url = result['response']['upload_url']

			# Загружаем изображение на url
			response = requests.post(upload_url, files=img, verify=False)
			result = json.loads(response.text)


			# Сохраняем фото на сервере и получаем id
			method_url = 'https://api.vk.com/method/photos.saveWallPhoto?'
			data = { "v" : apiVersion, "access_token": userToken, "gid":int(pageID),  "photo":result['photo'], "hash":result['hash'], "server":result['server'] }
			response = requests.post(method_url, data, verify=False)
			
			print(response.text)
			result = json.loads(response.text)
			media_id = result['response'][0]['id']
			owner_id = result['response'][0]['owner_id']

			options["attachments"]="photo{}_{}".format(owner_id, media_id)

		except Exception as e:
			print("Problem posting image!")
			print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
			print ("#######################")
			return -1;

	if link != None:
		options["attachments"] = urlEncodeNonAscii(link)

	result = curl_post("https://api.vk.com/method/wall.post", options)

	print(result)
	result = json.loads(result)

	if ("error" in result and result["error"]["error_code"] == 214):
		print("Over vk post limit, will try again later!")
		return result["error"]["error_code"]

	return 0
