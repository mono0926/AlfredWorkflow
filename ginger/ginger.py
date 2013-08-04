#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import sys
import os

class GingerSummary(object):
	"""Ginger Summary"""
	def __init__(self, original, results):
		super(GingerSummary, self).__init__()
		self.original = original
		self.results = sorted(results, cmp=lambda x, y: cmp(x.from_, y.from_))
		self.gingered = None

	def process(self):
		if not self.gingered:
			self._ginger()
		return self.gingered;

	def show_detail(self):
		for r in self.results:
			print(r)

	def _ginger(self):
		gingered = self.original
		offset = 0
		for i, r in enumerate(self.results):
			suggest = r.suggestions[0]
			gingered = '{0}{1}{2}'.format(gingered[:r.from_+offset], suggest, gingered[r.to+1+offset:])
			offset += len(suggest) - (r.to - r.from_ + 1)
		self.gingered = gingered


class GingerResult(object):
	"""Ginger Result"""
	def __init__(self):
		super(GingerResult, self).__init__()

	@classmethod
	def create_from_json(cls, json):
		that = GingerResult()
		that.from_ = json['From']
		that.to = json['To']
		that.suggestions = [x['Text'] for x in json['Suggestions']]
		that.should_replace = bool(json['ShouldReplace'])
		that.confidence = json['Confidence']
		return that

	def __str__(self):
		return 'from: {0}, to: {1}, suggestions: [{2}], should_replace: {3}, confidence: {4}'.format(
			self.from_, self.to, ', '.join(self.suggestions), self.should_replace, self.confidence)

class GingerClient(object):
	"""Ginger Client"""
	base_url = 'http://services.gingersoftware.com/Ginger/correct/json/GingerTheText'
	api_key = '6ae0c3a0-afdc-4532-a810-82ded0054236'
	def __init__(self, sentence):
		super(GingerClient, self).__init__()
		self.sentence = sentence
	
	def ginger(self):
		self._initialize()
		return self.summary.process()

	def show_detail(self):
		self._initialize()
		self.summary.show_detail()

	def _initialize(self):
		params = {'apiKey':GingerClient.api_key, 'text':self.sentence, 'lang':'US', 'clientVersion':'2.0'}
		response = requests.get(GingerClient.base_url, params=params)
		results = json.loads(response.text)['LightGingerTheTextResult']
		ginger_results = [GingerResult.create_from_json(x) for x in results]
		self.summary = GingerSummary(self.sentence, ginger_results)	


# if __name__ == '__main__':
# 	sentence = 'I am programmer and writing bad english. I am japanese.'
# 	args = sys.argv
# 	if len(args) == 2:
# 		sentence = args[1]
# 	client = GingerClient(sentence)
# 	gingered = client.ginger()
# 	item = workflow.WorkflowItem(gingered, 'Gingered sentence')
# 	generator = workflow.WorkflowGenerator([item])
# 	xml = generator.export()
# 	print(xml)