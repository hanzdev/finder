#! /usr/bin/python3
# -*- coding: UTF-8 -*-
# github/hanzdev

import requests
import argparse
from colorama import Fore


if __name__ == "__main__":

	def banner():
		banner = """
    ____   _                 __
   / __/  (_)  ____     ____/ /  ___     _____
  / /_   / /  / __ \   / __  /  / _ \   / ___/
 / __/  / /  / / / /  / /_/ /  /  __/  / /
/_/    /_/  /_/ /_/   \__,_/   \___/  /_/

     Admin Panel and Subdomain Finder.
	     github/hanzdev
	"""

		print(Fore.GREEN + banner)
	banner()


	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--domain', help="Target domain.", dest="domain", required=True)
	parser.add_argument('-t', '--type', help="Choose option.", dest="type", required=True,\
						 choices=["adminp", "subdomain"])
	parser.add_argument('-p', '--protocol', help="Choose protocol", dest='protocol', required=True, \
					choices=["http", "https"])

	parser.add_argument('-f', '--file', help="Path of list.", dest="path", required=True)

	args = parser.parse_args()
	dmn = (args.domain)
	opt = (args.type)
	proto = (args.protocol)
	fm = (args.path)

	def subdomain_finder():
		#file = open('subdomains.txt', 'r')
		file = open(fm, 'r')
		ctx = file.read()
		subdomains = ctx.splitlines()

		for subdomain in subdomains:
			url = f'{proto}://{subdomain}.{dmn}'
		try:
			requests.get(url)
		except requests.ConnectionError:
			pass
		else:
			print(Fore.CYAN + "Discovered Subdomain: ", url)


	def adminpanel_finder():
		#file2 = open('panels.txt', 'r')
		file2 = open(fm, 'r')
		ctt = file2.read()
		panels = ctt.splitlines()

		for panel in panels:
			url2 = f'{proto}://{dmn}/{panel}'
		try:
			requests.get(url2)
		except requests.ConnectionError:
			pass
		else:
			print(Fore.CYAN + "Discovered Admin Panels: ", url2)


	if args.type == "subdomain":
		subdomain_finder()
	elif args.type == "adminp":
		adminpanel_finder()
	else:
		print("Invalid value.")
