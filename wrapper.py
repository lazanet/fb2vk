#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, os
while True:
	os.system("python3 ./main.py > ./log.txt 2>&1")
	print("Done one turn!")
	time.sleep(600)
