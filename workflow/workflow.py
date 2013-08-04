#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from xml.etree.ElementTree import *
from xml.dom import minidom
import uuid

class WorkflowItem(object):
	"""Workflow Item"""
	def __init__(self, title, subtitle, icon=None):
		super(WorkflowItem, self).__init__()
		self.title = title
		self.subtitle = subtitle
		self.icon = icon

class WorkflowGenerator(object):
	"""Workflow Generator"""
	def __init__(self, items):
		super(WorkflowGenerator, self).__init__()
		self.items = items

	def export(self):
		items = Element('items')
		for wItem in self.items:
			item = SubElement(items, 'item', {'uid': str(uuid.uuid1()), 'arg': wItem.title})
			title = SubElement(item, 'title')
			title.text = wItem.title
			subtitle = SubElement(item, 'subtitle')
			subtitle.text = wItem.subtitle
			icon = SubElement(item, 'icon')
			icon.text = wItem.icon
		return self.prettify(items)
		
	def prettify(self, elem):
	    """Return a pretty-printed XML string for the Element.
	    """
	    rough_string = tostring(elem, 'utf-8')
	    reparsed = minidom.parseString(rough_string)
	    return reparsed.toprettyxml(indent="  ")
