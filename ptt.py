#coding=utf-8
import os
import sys
import time
import json
import telnetlib

# var
HOST = 'ptt.cc'
PATH = os.path.dirname(os.path.abspath(__file__))

class PTT:
	def __init__(self, var):
		self.account = var['account']
		self.password = var['password']
		self.talnet = None

	def login(self):
		# init
		self.telnet = telnetlib.Telnet(HOST)
		time.sleep(5)

		reponse = self.telnet.read_very_eager().decode('big5','ignore')
		
		if u'系統過載' in reponse :
			print('[Login] System overloading')
			exit()

		if u'請輸入代號' in reponse:
			print('[Login] Enter account')
			self.telnet.write((self.account + '\r\n').encode('ascii'))
			time.sleep(5)
			print('[Login] Enter password')
			self.telnet.write((self.password + '\r\n').encode('ascii'))
			time.sleep(5)

			reponse = self.telnet.read_very_eager().decode('big5','ignore')
			
			if u'密碼不對' in reponse:
				 print('[Login] Wrong password')
				 exit()
				 reponse = self.telnet.read_very_eager().decode('big5','ignore')
			
			if u'您想刪除其他重複登入' in reponse:
				 print('Remove duplicate connection')
				 self.telnet.write('y\r\n'.encode('ascii'))
				 time.sleep(5)
				 reponse = self.telnet.read_very_eager().decode('big5','ignore')
			
			if u'請按任意鍵繼續' in reponse:
				 print('[Login] Enter to continue')
				 self.telnet.write('\r\n'.encode('ascii'))
				 time.sleep(5)
				 reponse = self.telnet.read_very_eager().decode('big5','ignore')
			
			if u'您要刪除以上錯誤嘗試' in reponse:
				 print('[Login] Delete wrong connection record')
				 self.telnet.write('y\r\n'.encode('ascii'))
				 time.sleep(5)
				 reponse = self.telnet.read_very_eager().decode('big5','ignore')
			print('[Login] Done')
		else:
			print('[Login] Error')

	def logout(self) :
		self.telnet.write('qg\r\ny\r\n'.encode('ascii'))
		time.sleep(5)
		self.telnet.close()
		print('[Logout] Done')

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
		print('Missing config file')
		exit()

	# run script
	for i in configs:
		ptt = PTT(i)
		ptt.login()
		ptt.logout()
		time.sleep(10)