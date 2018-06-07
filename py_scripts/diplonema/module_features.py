#!/usr/bin/env python3
import os
from collections import OrderedDict

os.chdir('/home/kika/MEGAsync/diplonema_mt/comparison/')
table = open('1618_multi_modules.tsv')
out = open('1618_multi_modules_stat.tsv', 'w')

def in_range(start, number, end):
	return start <= number <= end

contigs = OrderedDict(list())
for line in table:
	try:
		name = line.split('\t')[0]
		module = line.split('\t')[1]
		mmin = int(line.split('\t')[2])
		mmax = int(line.split('\t')[3])
		strand = line.split('\t')[5][:-1]
		if name not in contigs:
			contigs[name] = [(module, mmin, mmax, strand)]
		else:
			contigs[name].append((module, mmin, mmax, strand))
	except:
		pass

for key, value in contigs.items():
	if len(value) > 1:
		for i in range(len(value)):
			for j in range(i + 1, len(value)):
				if in_range(value[i][1], value[j][1], value[i][2]):
				#start J inside I
					if in_range(value[i][1], value[j][2], value[i][2]):
					#end J inside I => embedded J in I
						if value[i][3] == value[j][3]:
							out.write('{}\t{} [{}]\tsame\tembedded\n'.format(key, value[i][0], value[j][0]))
						else:
							out.write('{}\t{} [{}]\topposite\tembedded\n'.format(key, value[i][0], value[j][0]))
					else:
					#end J outside I => overlapping
						length = int(value[i][2]) - int(value[j][1]) + 1
						if value[i][3] == value[j][3]:
							out.write('{}\t{} + {} ({})\tsame\toverlapping\n'.format(key, value[i][0], value[j][0], length))
						else:
							out.write('{}\t{} + {} ({})\topposite\toverlapping\n'.format(key, value[i][0], value[j][0], length))
				elif in_range(value[i][1], value[j][2], value[i][2]):
				#end J inside I => overlapping
					length = int(value[j][2]) - int(value[i][1]) + 1
					if value[i][3] == value[j][3]:
						out.write('{}\t{} + {} ({})\tsame\toverlapping\n'.format(key, value[j][0], value[i][0], length))
					else:
						out.write('{}\t{} + {} ({})\topposite\toverlapping\n'.format(key, value[j][0], value[i][0], length))
				elif in_range(value[j][1], value[i][1], value[j][2]) and in_range(value[j][1], value[i][2], value[j][2]):
				#embedded I in J
					if value[j][3] == value[i][3]:
						out.write('{}\t{} [{}]\tsame\tembedded\n'.format(key, value[j][0], value[i][0]))
					else:
						out.write('{}\t{} [{}]\topposite\tembedded\n'.format(key, value[j][0], value[i][0]))

out.close()