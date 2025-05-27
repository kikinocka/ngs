#!/usr/bin/env python3
import os

os.chdir('/mnt/mokosz/home/kika/metamonads/ancestral_OGs/final_trees/')
trees = [x for x in os.listdir() if x.endswith('.aln_renamed.tre')]

# names = open('/mnt/mokosz/home/kika/allDB/all.seq_dict.upd.tsv')
names = open('/mnt/mokosz/home/kika/metamonads/ancestral_OGs/OGs.seq_dict.upd.tsv')

name_dict = {}
for name in names:
	split_line = name.strip().split('\t')
	new = split_line[0]
	# new = split_line[0] + ' ' + split_line[1]
	name_dict[split_line[1]] = new
# print(name_dict)

for tree in trees:
	print(tree)
	name = tree.split('.tre')[0]
	# with open('{}_renamed.tre'.format(name), 'w') as result:
	with open('{}2.tre'.format(name), 'w') as result:
		for tree_line in open(tree):
			orgn_dirty = tree_line.strip().split(',')
			for orgn in orgn_dirty:
				orgn_clean = orgn.split(':')[0].replace('(', '').split('__eval')[0]
				if orgn_clean in name_dict.keys():
					tree_line = tree_line.replace(orgn_clean, name_dict[orgn_clean])
		result.write(tree_line)
