#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
from optparse import OptionParser

def output_message():	
	parser = OptionParser()
	parser.add_option("-m", "--message", )
	(options, args) = parser.parse_args()
	wait_length = args[0]
	wait_unit = args[1]
	unit_dict = {'s': 'second', 'm': 'minute', 'h': 'hour'}
	if wait_length != 1:
		for k in unit_dict.keys():
			unit_dict[k] += 's'

	pre_message = 'You\'ll be notified {0} {1} later.'.format(wait_length, unit_dict[wait_unit])
	print(pre_message)

try:
	output_message()
except Exception, e:
	print(e)