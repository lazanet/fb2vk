import os
from datetime import datetime

folder = os.path.dirname(os.path.realpath(__file__))
errors = ""

def getTimeFile(name):
	timestamp = nowTime = str(datetime.now())
	try:
		dirs = os.path.join(folder, "logs")
		path = os.path.join(dirs, name+".txt")

		if not os.path.exists(dirs):
			os.makedirs(dirs, exist_ok = True)

		if os.path.exists(path):
			with open(path, "r") as f:
				timestamp = f.read().strip()
	except:
		print("IO еrror")
	return datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')

def saveTimeFile(name, time):
	with open(os.path.join(folder, "logs", name+".txt"), "w") as f:
		f.write(str(time))

def reportError(message):
	message += "\n"
	print ("Error: "+message)
	errors += message

def reportErrorEnd(vk):
	if errors!="":
		vk.post(reportLoc, errors)
