# -*- coding: utf-8 -*- 
"""
@author: Ilshat Fattakhov
@contact: https://vk.com/ilshat.fattakhov
"""
import numpy as np
from math import ceil
import time
import pickle
import os
import random

debug = False

container = {'x':30, 'y':40, 'z':50, type:'train', 'etc':'some extra parameters'}
boxes = [
			{'x':5, 'y':25, 'z':10},
			{'x':15, 'y':5, 'z':10}, 
			{'x':15, 'y':5, 'z':20}, 
			{'x':10, 'y':15, 'z':10}
		]
# class Box(self): #self, 'x', 'y', 'z'):
# 	self.x = 'x'
# 	self.y = 'y'
# 	self.z = 'z'

#тупо перебираем возможные варинты
B1 = boxes[0]
B2 = boxes[1]
def combine_2_boxes(b1, b2):
	
	combined_boxes_list = []
	
	return (b2)
def main():
	print combine_2_boxes(B1,B2)

main()