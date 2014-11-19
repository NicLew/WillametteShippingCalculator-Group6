#!/usr/bin/python3

################################
# File Name:	test_SaleItemUnitTest.py
# Author:		Chadd Williams
# Date:			11/17/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		Unittest for SaleItem
################################


import unittest
from ShippingLogic import *
from basket import Basket
from SaleItem import SaleItem

class TestShippingLogic(unittest.TestCase):
	
	def setUp(self):
		""" the text fixture, necessary setup for the tests to run
		"""
		self.theShippingObj = ShippingLogic()
		self.theBasket = Basket()
		
		
	def tearDown(self):
		""" nothing to tear down here
		If your test created a database or built a network connection
		you might delete the database or close the network connection
		here. You might also close files you opened, close your
		TK windows if this is GUI program, or kill threads if this is
		a multithreaded application
		"""
		pass # nothing to do
		
	def test_calcWeightForCost(self):
		self.assertEqual(self.theShippingObj.calcWeightForCost(self.theBasket), 0)
		
		self.theBasket.addItem((1, SaleItem(['10', '2', 'TestItem'])))
		self.assertEqual(self.theShippingObj.calcWeightForCost(self.theBasket), 2)
		
	def test_calcCostForShippingByWeight(self):
		self.assertEqual(self.theShippingObj.calcCostForShippingByWeight(.1), 5)
		self.assertEqual(self.theShippingObj.calcCostForShippingByWeight(1), 7)
		self.assertEqual(self.theShippingObj.calcCostForShippingByWeight(5), 10)
		self.assertEqual(self.theShippingObj.calcCostForShippingByWeight(101), 0)
