#coding=utf-8
from ptt.cli import *
from ptt.utils import Client

# pattern
pattern_except = '{func:>10} {exception}'

def main():
	# var
	args = parse_argv()
	client = Client(args['account'], args['password'])

	if args['command'] == 'login':
		try:
			client.login()
			client.logout()
		except Exception as e:
			print(pattern_except.format(func=args['mode'], exception=str(e)))
	elif args['command'] == 'post':
		try:
			# init
			if args['file']:
				with open(args['file'], 'r') as file:
					args['content'] = ''.join(file.readlines())

			args['content'] = args['content'].replace('\n', '\r\n')
					
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