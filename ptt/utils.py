#coding=utf-8
import os
import sys
import time
import json
import telnetlib

# constant
HOST = 'ptt.cc'
PATH = os.path.dirname(os.path.abspath(__file__))

# pattern
pattern_log = '{func:>10} {content}'

class Client:
	def __init__(self, account, password):
		self.account = account
		self.password = password
		self.telnet = telnetlib.Telnet(HOST)
		time.sleep(3)

	def login(self):
		# log
		print(pattern_log.format(func='login', content=self.account))
		
		# check login
		response = self.telnet.read_very_eager().decode('big5','ignore')
		
		if u'系統過載' in response :
			print(pattern_log.format(func='login', content='system overload'))
			exit()

		if u'請輸入代號' in response:
			print(pattern_log.format(func='login', content='entering account'))
			self.telnet.write((self.account + '\r\n').encode('big5'))
			time.sleep(3)
			print(pattern_log.format(func='login', content='typing password'))
			self.telnet.write((self.password + '\r\n').encode('big5'))
			time.sleep(3)

			response = self.telnet.read_very_eager().decode('big5','ignore')
			
			if u'密碼不對' in response:
				print(pattern_log.format(func='login', content='wrong password'))
				exit()
				
			if u'您想刪除其他重複登入' in response:
				print(pattern_log.format(func='login', content='remove duplicate connection'))
				self.telnet.write('y\r\n'.encode('big5'))
				time.sleep(3)
				
			if u'請按任意鍵繼續' in response:
				self.telnet.write('\r\n'.encode('big5'))
				time.sleep(3)
				response = self.telnet.read_very_eager().decode('big5','ignore')
			
			if u'您要刪除以上錯誤嘗試' in response:
				print(pattern_log.format(func='login', content='clear error tries'))
				self.telnet.write('y\r\n'.encode('big5'))
				time.sleep(3)

			print(pattern_log.format(func='login', content='success'))
		else:
			print(pattern_log.format(func='login', content='failed'))

	def logout(self):
		# log
		print(pattern_log.format(func='logout', content=self.account))
		
		self.telnet.write('qg\r\ny\r\n'.encode('big5'))
		self.telnet.close()
		
		# log
		print(pattern_log.format(func='logout', content='success'))

	def post(self, var):
		# var
		post = None

		# select board
		self.telnet.write('s'.encode('big5'))
		time.sleep(3)
		self.telnet.write((var['board'] + '\r\n').encode('big5'))
		time.sleep(3)

		# enter to continue
		response = self.telnet.read_very_eager().decode('big5','ignore')
		if u'請按任意鍵繼續' in response:
			self.telnet.write('\r\n'.encode('big5'))
			time.sleep(3)
				
		# ctrl+p
		self.telnet.write('\x10'.encode('big5'))
		time.sleep(3)

		# category
		self.telnet.write((str(var['type']) + '\r\n').encode('big5'))
		time.sleep(3)

		# write title
		self.telnet.write((var['title'] + '\r\n').encode('big5'))
		time.sleep(3)

		# write content
		for c in var['content']:
			self.telnet.write((c).encode('big5'))
			time.sleep(1)
		self.telnet.write('\x18'.encode('big5'))
		time.sleep(3)

		# save content
		self.telnet.write('s\r\n'.encode('big5'))
		time.sleep(3)

		# signature
		self.telnet.write('0\r\n'.encode('big5'))
		time.sleep(3)

		print(pattern_log.format(func='post', content='success'))