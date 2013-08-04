#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import sys
import os
from ginger.ginger import *
from workflow.workflow import *

def output_ginger(sentence):
	client = GingerClient(sentence)
	gingered = client.ginger()
	item = WorkflowItem(gingered, 'Gingered sentence')
	generator = WorkflowGenerator([item])
	xml = generator.export()
	print(xml)

def output_rephrase(sentence):
	rephraser = RephraseClient(sentence)
	rephraseds = rephraser.rephrase()
	items = [WorkflowItem(x, 'Rephrased sentence') for x in rephraseds]
	generator = WorkflowGenerator(items)
	xml = generator.export()
	print(xml)

if __name__ == '__main__':
	sentence = 'I am programmer and writing bad english. I am japanese.'
	args = sys.argv
	if len(args) == 1:
		output_ginger(sentence)	

	elif len(args) == 3:
		sentence = args[2]
		if args[1] == 'ginger':
			output_ginger(sentence)
		elif args[1] == 'rephrase':
			output_rephrase(sentence)