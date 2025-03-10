#!/usr/bin/env python3
import os

os.chdir('/mnt/mokosz/home/kika/workdir/')
trees = [x for x in os.listdir() if x.endswith('.aln.treefile')]

#file in format Acc. number \t name of organism \n
names = open('/mnt/mokosz/home/kika/metamonads/MRO_proteins/metamonads_assemblies/all.seq_dict.tsv')

name_dict = {}
for name in names:
	split_line = name.strip().split('\t')
	new = split_line[1]
	# new = split_line[0] + ' ' + split_line[1]
	name_dict[split_line[0]] = new
# print(name_dict)

# for tree in trees:
# 	print(tree)
# 	# name = tree.split('.tre')[0] + tree.split('.tre')[1]
# 	name = tree
# 	tree_line = open(tree).readline()
# 	for key in name_dict:
# 		tree_line = tree_line.replace(key, name_dict[key])
# 	with open('{}_renamed.tre'.format(name), 'w') as result:
# 		result.write(tree_line)


for tree in trees:
	print(tree)
	# name = tree.split('.treefile')[0]
	name = tree.split('.tre')[0]
	# name = tree.split('.tre')[0] + tree.split('.tre')[1]
	with open('{}_renamed.tre'.format(name), 'w') as result:
		for tree_line in open(tree):
			for key in name_dict:
				tree_line = tree_line.replace(key, name_dict[key])
			result.write(tree_line)
