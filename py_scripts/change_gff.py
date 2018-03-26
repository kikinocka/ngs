#!/usr/bin/env python3
import os

os.chdir('/home/kika/MEGAsync/blasto_project/orthofinder/sg_ogs/jac_renamed/')
gff = open('p57_ins_only.gff')

with open('p57_ins_renamed.gff', 'w') as out:
	for line in gff:
		new_third = line.split('\t')[8].split('ID=')[1][:-1]
		new_line = line.replace(line.split('\t')[2], new_third)
		out.write(new_line)