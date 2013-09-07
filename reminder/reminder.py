#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#print('abd')
import time
from optparse import OptionParser


def output_message():	
	parser = OptionParser()
	parser.add_option("-m", "--message", )

	(options, args) = parser.parse_args()

	wait_length = float(args[0])
	wait_unit = args[1]

	wait_length_in_seconds = 0.0
	if wait_unit == 's':
		wait_length_in_seconds = wait_length * 1.0
	elif wait_unit == 'm':
		wait_length_in_seconds = wait_length * 60.0
	elif wait_unit == 'h':
		wait_length_in_seconds = wait_length * 3600.0
	else:
		print('Error occured! Specify timeunit as s, m, or h.(ex: "remind 5 m -m "this is message"")')

	time.sleep(wait_length_in_seconds)
	message = options.message
	print(message)

try:
	output_message()
except Exception, e:
	print(e)