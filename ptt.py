#coding=utf-8
import os
import sys
import time
import json
import telnetlib

from ptt.cli import *
from ptt.utils import Client

# pattern
pattern_except = '{func:>10} {exception}'

def main():
	# var
	args = parse_argv()
	client = Client(args['account'], args['password'])

	print(args)

	if args['mode'] == 'login':
		try:
			client.login()
			client.logout()
		except Exception as e:
			print(pattern_except.format(func=args['mode'], exception=str(e)))
	elif args['mode'] == 'post':
		try:
			# init
			if args['file']:
				with open(args, 'r') as file:
					args['content'] = file.read()

			client.login()
			client.post({
				'board': args['board'],
				'type': args['type'],
				'article': args['article'],
				'content': args['content']
			})
			client.logout()
		except Exception as e:
			print(pattern_except.format(func=args['mode'], exception=str(e)))

if __name__ == '__main__':
	main()