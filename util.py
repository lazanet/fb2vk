import os
from datetime import datetime

from config import *
from multiprocessing import Pool, Value, Array, Manager

manager = Manager()
folder = os.path.dirname(os.path.realpath(__file__))
errors = manager.dict()
errors["msg"] = ""

def get_time_file(name):
	timestamp = str(datetime.now())
	try:
		dirs = os.path.join(folder, "logs")
		path = os.path.join(dirs, name+".txt")

		if not os.path.exists(dirs):
			os.makedirs(dirs, exist_ok = True)

		if os.path.exists(path):
			with open(path, "r") as f:
				timestamp = f.read().strip()
	except:
		report_error("IO error while opening time file for {}".format(name))
	try:
		d = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
	except:
		d = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
	return d

def save_time_file(name, time):
	with open(os.path.join(folder, "logs", name+".txt"), "w") as f:
		f.write(str(time))

def report_exception(msg, e):
	report_error(msg + ", exception was: \n" + str(e))

def report_error(message):
	global errors
	message += "\n"
	print ("Error: {}".format(message))
	errors["msg"] += message

def report_error_end(vk):
	global errors
	global report_loc
	global report_user_token
	if errors["msg"] != "":
		vk.post(report_loc, report_user_token,  errors["msg"])
	else:
		print("There were no errors!")

def info(msg):
	print()
	print(msg)
	print()
