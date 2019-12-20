#!/usr/bin/env python3
import os

os.chdir('/home/kika/MEGAsync/diplonema/cardiolipin/phospholipasesD/')

#file in format Acc. number \t name of organism \n
names = open('phospholipasesD_names.txt')
tree = open('phospholipasesD_trimal_0.5.aln.treefile')

name_dict = {}
for name in names:
	split_line = name.split('\t')
	name_dict[split_line[0]] = split_line[0] + ' ' + split_line[1][:-1]

tree_line = tree.readline()

for key in name_dict:
	tree_line = tree_line.replace(key, name_dict[key])

#2 ways of writting results to the file:
##1) can't forget to close the file in the end of the code
##result = open('Tree_renamed.txt', 'w')
##result.write(tree_line)
##result.close()

#2) closes result file automatically
with open('phospholipasesD_renamed.tree', 'w') as result:
	result.write(tree_line)
