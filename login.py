#coding=utf-8
import os
import sys
import time
import json
import telnetlib

from ptt import Ptt

# constant
PATH = os.path.dirname(os.path.abspath(__file__))

def load_config():
	with open(PATH + '/config.json', 'r') as config_file:
		config = json.load(config_file)
	return config
		 
if __name__=='__main__' :
	# var
	configs = None

	# init
	try:
		configs = load_config()
	except:
		print('[%10s] %s' % ('Error', 'load_config()'))
		exit()

	# run script
	for i in configs:
		ptt = Ptt.Object(i)
		ptt.login()
		ptt.logout()
		time.sleep(5)