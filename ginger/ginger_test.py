#!/usr/local/bin/python

import unittest
from mock import MagicMock
from mocker import Mocker, MockerTestCase
import ginger

class GingerSummaryTest(unittest.TestCase):

	def setUp(self):
		result1 = ginger.GingerResult()
		result1.from_ = 5
		result1.to = 14
		result1.suggestions = ["a programmer"]
		result1.should_replace = True
		result1.confidence = 4
		result2 = ginger.GingerResult()
		result2.from_ = 32
		result2.to = 38
		result2.suggestions = ["English"]
		result2.should_replace = True
		result2.confidence = 4
		
		self.summary = ginger.GingerSummary('I am programmer and writing bad english.', [result1, result2])

	def test_export(self):
		gingered = self.summary.process()
		self.assertEqual(gingered, 'I am a programmer and writing bad English.')

class GingerResultTest(unittest.TestCase):

	def setUp(self):
		self.json = {'From': 3, 'To': 5, 'Suggestions': [{'Text': 'suggested'}], 'ShouldReplace': 'True', 'Confidence': 4}

	def test_create_from_json(self):
		result = ginger.GingerResult.create_from_json(self.json)
		self.assertEqual(result.from_, 3)
		self.assertEqual(result.to, 5)
		self.assertEqual(result.suggestions, ['suggested'])
		self.assertTrue(result.should_replace)
		self.assertEqual(result.confidence, 4)

class GingerClientTest(MockerTestCase):

	# def setUp(self):

	def test_ginger(self):
		result = self.mocker.mock()
		result.text
		self.mocker.result('{"LightGingerTheTextResult":[{"Confidence":4,"From":0, "ShouldReplace":true,"Suggestions":[{"LrnCatId":45,"Text":"g"}],"To":1}]}')
		myget = self.mocker.replace("requests.get")
		myget('http://services.gingersoftware.com/Ginger/correct/json/GingerTheText', 
			params={'apiKey':'6ae0c3a0-afdc-4532-a810-82ded0054236', 'text':'sentence', 'lang':'US', 'clientVersion':'2.0'})
		self.mocker.result(result)
		self.mocker.replay()
		self.client = ginger.GingerClient('sentence')
		gingered = self.client.ginger()
		self.assertEqual(gingered, 'gintence')
		self.mocker.verify()


if __name__ == '__main__':
	unittest.main()