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

	if len(sys.argv) != 2:
		print('[%10s] %s' % ('Usage', '<post.json>'))
		exit()

	# init
	try:
		configs = load_config()
	except:
		print('[%10s] %s' % ('Error', 'load_config()'))
		exit()

	# run script
	ptt = Ptt.Object(configs[0])

	try:
		ptt.login()
	except Exception as e:
		print('[%10s] %s' % ('Error', str(e)))

	try:
		ptt.post(sys.argv[1])
	except Exception as e:
		print('[%10s] %s' % ('Error', str(e)))

	try:
		ptt.logout()
	except Exception as e:
		print('[%10s] %s' % ('Error', str(e)))
	
	time.sleep(5)