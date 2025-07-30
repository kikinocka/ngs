#!/usr/bin/env python3
import os

os.chdir('/mnt/mokosz/home/kika/metamonads/MRO_proteins/')
trees = [x for x in os.listdir() if x.endswith('.treefile')]

# names = open('/mnt/mokosz/home/kika/metamonads/MRO_proteins/metamonads_assemblies/all.seq_dict_renamed.tsv')
names = open('/mnt/mokosz/home/kika/allDB/all.seq_dict.upd.tsv')
# names = open('/mnt/mokosz/home/kika/allDB/bacteria/bct.seq_dict.upd.tsv')

name_dict = {}
for name in names:
	split_line = name.strip().split('\t')
	new = split_line[0]
	# new = split_line[0] + ' ' + split_line[1]
	name_dict[split_line[1]] = new
# print(name_dict)

for tree in trees:
	print(tree)
	name = tree.split('.')[0]
	with open('{}.final_renamed.tre'.format(name), 'w') as result:
		for tree_line in open(tree):
			orgn_dirty = tree_line.strip().split(',')
			for orgn in orgn_dirty:
				orgn_clean = orgn.split(':')[0].replace('(', '').split('_eval')[0]
				if orgn_clean in name_dict.keys():
					tree_line = tree_line.replace(orgn_clean, name_dict[orgn_clean])
		result.write(tree_line)
