#!/usr/bin/env python3
import os
from collections import defaultdict, OrderedDict

os.chdir('/home/kika/ownCloud/blastocrithidia/seqfire/')
files = sorted(os.listdir())

def get_ins_len(file):
	ins_dict = defaultdict(list)
	len_dict = OrderedDict()
	print(file)
	for line in open(file):
		gene = line.split('\t')[0]
		ins = int(line.split('\t')[3])
		ins_dict[gene].append(ins)
	for key, value in ins_dict.items():
		total = 0
		for i in value:
			total += i
		len_dict[key] = total
	return len_dict


with open('indel_len.txt', 'w') as out:
	for file in files:
		if file.endswith('.tsv'):
			out.write('{}\n'.format(file.split('.')[0].split('_')[2]))
			ins_len = get_ins_len(file)
			for key, value in ins_len.items():
				out.write('{}\t{}\n'.format(key, value))
