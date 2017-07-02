#coding=utf-8
import os
import sys
import time
import json
import telnetlib

from ptt.cli import *
from ptt.utils import Client

def main():
	args = parse_argv()

	print(args)

	client = Client(args['account'], args['password'])

	client.login()
	client.logout()

if __name__ == '__main__':
	main()