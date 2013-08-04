#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import sys
import os
from ginger.ginger import *
from workflow.workflow import *

if __name__ == '__main__':
	sentence = 'I am programmer and writing bad english. I am japanese.'
	args = sys.argv
	if len(args) == 2:
		sentence = args[1]
	client = GingerClient(sentence)
	gingered = client.ginger()
	item = WorkflowItem(gingered, 'Gingered sentence')
	generator = WorkflowGenerator([item])
	xml = generator.export()
	print(xml)