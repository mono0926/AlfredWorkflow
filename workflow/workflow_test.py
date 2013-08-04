#!/usr/local/bin/python

import unittest
import workflow

class TestWorkflowGenerator(unittest.TestCase):

	def setUp(self):
		item = workflow.WorkflowItem('title', 'subtitle')
		self.generator = workflow.WorkflowGenerator([item])

	def test_export(self):
		xml = self.generator.export();
		print(xml)

if __name__ == '__main__':
	unittest.main()