#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/trees/metazoa_myxozoa/placement/')
jplacef = [x for x in os.listdir() if x.endswith('.accumulated.jplace')]


for jplace in jplacef:
	place_dict = {}
	for line in open(jplace):
		line = line.replace(' ', '')
		if line.startswith('['):
			placement = line.replace('[', '').split(',')[0]
			if placement not in place_dict:
				place_dict[placement] = 1
			else:
				place_dict[placement] += 1
		else:
			pass
	print(place_dict)