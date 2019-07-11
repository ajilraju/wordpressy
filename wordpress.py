#! /usr/bin/env python3

import requests
import sys
import json
import random

class colors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


description = colors.FAIL + '''To use this tool, run "python3 wordpressy.py TARGET_IP" NOTE: User agents are spoofed''' + colors.ENDC

directories = ['/wp-admin','/wp-content','/wp-includes','/wp-login.php','/wp-load.php', '/wp-config.php']

with open('config_web_enum.json') as f:
	useragents = json.load(f)

def enumerate(target):

	fail_count = 0
	print(description, end="\n")

	random_user_agent = random.choice(useragents["user agents"])
	headers = {'user-agent': random_user_agent}

	for d in directories:
			r = requests.get(f'http://{target}{d}', headers=headers)
			if '404' and 'Not Found' in r.text:
					fail_count += 1
					print(colors.WARNING + target + d + " does not exist" + colors.ENDC)
			else:
					print(colors.OKGREEN + "Found directory: " + target + d + colors.ENDC)	
	if fail_count >= 6:
		print()
		print(colors.FAIL + "Matching Failed!!!" + colors.ENDC)
	else:	
		print()	
		print(colors.BOLD + "Matching success!!!. It's wordpress site." + colors.ENDC)


def main():
	if len(sys.argv) > 1:
		enumerate(sys.argv[1])
	else:
		print(description)

if __name__ == '__main__':
	main()
