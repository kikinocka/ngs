#!/usr/bin/env python3

import os

os.chdir('/storage/brno3-cerit/home/kika/elonga_bct_genomes/')
files = [x for x in os.listdir() if x.endswith('.tblastn.out')]

with open('bct_SDR_a4.presence.tsv', 'w') as result:
	for file in files:
		print(file)
		for line in open(file):
			if line.startswith('#'):
				pass
			else:
				if float(line.split('\t')[10]) < 0.001:
					new_line = '{}\t1\t{}\n'.format(file.split('_')[0]+file.split('_')[1], line.split('\t')[10])
					result.write(new_line)
