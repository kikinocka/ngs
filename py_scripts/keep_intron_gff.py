#!/usr/bin/env python3
import os

os.chdir('/home/kika/MEGAsync/blasto_project/orthofinder/sg_ogs/jac_renamed/')
gff = open('p57_insertions.gff')

with open('p57_only_ins_renamed.gff', 'w') as out:
	for line in gff:
		if line.split('\t')[2] == 'intron':
			og = line.split('\t')[8].split('=')[1].split(';')[0]
			ins_name = line.split('\t')[8].split('ID=')[1][:-1]
			new_line = line.replace(line.split('\t')[2], '{} {}'.format(og, ins_name))
			out.write(new_line)