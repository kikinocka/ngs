#!/usr/bin/env python3
import os

os.chdir('/home/kika/MEGAsync/blasto_project/orthofinder/sg_ogs/jac_renamed/')
gff = open('p57_insertions.gff')

with open('p57_ins_only.gff', 'w') as out:
	for line in gff:
		if line.split('\t')[2] == 'intron':
			out.write(line)