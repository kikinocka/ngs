#!/usr/bin/env python3
import os

os.chdir('/mnt/mokosz/home/kika/metamonads/ancestral_OGs/final_trees/test/')
trees = [x for x in os.listdir() if x.endswith('.aln.treefile')]

#file in format Acc. number \t name of organism \n
names = open('/mnt/mokosz/home/kika/allDB/euk.seq_dict.tsv')

name_dict = {}
for name in names:
	split_line = name.strip().split('\t')
	new = split_line[0]
	# new = split_line[0] + ' ' + split_line[1]
	name_dict[split_line[1]] = new
# print(name_dict)

for tree in trees:
	print(tree)
	for tree_line in open(tree):
		orgn_dirty = tree_line.strip().split(',')
		for orgn in orgn_dirty.item():
			print(orgn.split(':')[0].replace('(', '').split('__eval')[0])
				
