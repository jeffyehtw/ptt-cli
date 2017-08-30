import argparse

# constant
__version__ = '1.0'
__description__ = 'ptt-cli - a command line tool for ptt.cc'
__epilog__ = 'Report bugs to <cjyeh@cs.nctu.edu.tw>'

def parse_argv():
	# init
	parser = argparse.ArgumentParser(
		description = __description__,
		epilog = __epilog__
	)

	# main parser
	parser.add_argument(
		'-v', '-V', '--version', 
		action = 'version', 
		help = 'Print program version', 
		version = 'v{}'.format(__version__)
	)

	# sub parser
	subparsers = parser.add_subparsers(
		dest = 'command',
		help = 'command help'
	)
	subparsers.required = True

	# login
	parser_login = subparsers.add_parser('login')
	parser_login.add_argument('account')
	parser_login.add_argument('password')

	# post
	parser_post = subparsers.add_parser('post')
	parser_post.add_argument('account')
	parser_post.add_argument('password')
	parser_post.add_argument('-b', '--board', required = True)
	parser_post.add_argument('-t', '--type', required = True)
	parser_post.add_argument('-a', '--article', required = True)
	parser_post.add_argument('-c', '--content', default = ' ')
	parser_post.add_argument('-f', '--file')

	results = parser.parse_args()

	return results.__dict__
