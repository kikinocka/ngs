#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/membrane-trafficking/trees/all_adaptors/ver4/combined/large-EGADZ/')
trees = [x for x in os.listdir() if x.endswith('raxml.tre')]

#file in format Acc. number \t name of organism \n
names = open('/Users/kika/ownCloud/membrane-trafficking/trees/all_adaptors/ver4/combined/large-EGADZ_codes_names.txt')

name_dict = {}
for name in names:
	split_line = name.strip().split('\t')
	new = split_line[1]
	# new = split_line[0] + ' ' + split_line[1]
	name_dict[split_line[0]] = new

# # print(name_dict)
# for tree in trees:
# 	print(tree)
# 	name = tree.split('.tre')[0]
# 	tree_line = open(tree).readline()
# 	for key in name_dict:
# 		tree_line = tree_line.replace(key, name_dict[key])
# 	with open('{}_renamed.tre'.format(name), 'w') as result:
# 		result.write(tree_line)


for tree in trees:
	print(tree)
	# name = tree.split('.tre')[0]
	name = tree.split('.tre')[0] + tree.split('.tre')[1]
	with open('{}_renamed.tre'.format(name), 'w') as result:
		for tree_line in open(tree):
			for key in name_dict:
				tree_line = tree_line.replace(key, name_dict[key])
			result.write(tree_line)
