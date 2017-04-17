import os
import time
import json
import telnetlib

# constant
HOST = 'ptt.cc'
PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

def load_post(file):
	with open(PATH + '/' + file, 'r') as file:
		post = json.load(file)
	return post

def load_content(file):
	with open(PATH + '/' + file, 'r') as file:
		lines = file.readlines()
	return lines

class Object:
	def __init__(self, var):
		self.account = var['account']
		self.password = var['password']
		self.telnet = telnetlib.Telnet(HOST)
		time.sleep(5)

	def login(self):
		print('[%10s] %s' % ('Login', self.account))
		# check login
		response = self.telnet.read_very_eager().decode('big5','ignore')
		
		if u'系統過載' in response :
			print('[%10s] %s' % ('Login', 'System overload'))
			exit()

		if u'請輸入代號' in response:
			print('[%10s] %s' % ('Login', 'Account'))
			self.telnet.write((self.account + '\r\n').encode('big5'))
			time.sleep(5)
			print('[%10s] %s' % ('Login', 'Password'))
			self.telnet.write((self.password + '\r\n').encode('big5'))
			time.sleep(5)

			response = self.telnet.read_very_eager().decode('big5','ignore')
			
			if u'密碼不對' in response:
				print('[%10s] %s' % ('Error', 'Wrong password'))
				exit()
				response = self.telnet.read_very_eager().decode('big5','ignore')
			
			if u'您想刪除其他重複登入' in response:
				print('[%10s] %s' % ('Login', 'Remove duplicated connection'))
				self.telnet.write('y\r\n'.encode('big5'))
				time.sleep(5)
				response = self.telnet.read_very_eager().decode('big5','ignore')
			
			if u'請按任意鍵繼續' in response:
				self.telnet.write('\r\n'.encode('big5'))
				time.sleep(5)
				response = self.telnet.read_very_eager().decode('big5','ignore')
			
			if u'您要刪除以上錯誤嘗試' in response:
				print('[%10s] %s' % ('Login', 'Clear error tries'))
				self.telnet.write('y\r\n'.encode('big5'))
				time.sleep(5)
				response = self.telnet.read_very_eager().decode('big5','ignore')
			print('[%10s] %s' % ('Login', 'Success'))
		else:
			print('[%10s] %s' % ('Error', 'Ptt.login()'))

	def logout(self) :
		print('[%10s] %s' % ('Logout', self.account))
		self.telnet.write('qg\r\ny\r\n'.encode('big5'))
		time.sleep(5)
		self.telnet.close()
		print('[%10s] %s' % ('Logout', 'Success'))

	def post(self, file):
		# var
		post = None

		# load config
		try:
			post = load_post(file)
		except Exception as e:
			print('[%10s] %s' % ('Error', str(e)))
			exit()

		# select board
		self.telnet.write('s'.encode('big5'))
		time.sleep(5)
		self.telnet.write((post['board'] + '\r\n').encode('big5'))
		time.sleep(5)

		# enter to continue
		response = self.telnet.read_very_eager().decode('big5','ignore')
		print(response)
		if u'請按任意鍵繼續' in response:
			self.telnet.write('\r\n'.encode('big5'))
			time.sleep(5)
				
		# ctrl+p
		self.telnet.write('\x10'.encode('big5'))
		time.sleep(5)

		# category
		self.telnet.write((str(post['category']) + '\r\n').encode('big5'))
		time.sleep(5)

		# write title
		self.telnet.write((post['title'] + '\r\n').encode('big5'))
		time.sleep(5)

		# write content
		for line in post['content']:
			self.telnet.write((line +'\r\n').encode('big5'))
			time.sleep(5)
		self.telnet.write('\x18'.encode('big5'))
		time.sleep(5)

		# save content
		self.telnet.write('s\r\n'.encode('big5'))
		time.sleep(5)

		# signature
		self.telnet.write('0\r\n'.encode('big5'))
		time.sleep(5)


		print('[%10s] %s' % ('Post', 'Success'))