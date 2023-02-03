#!/usr/bin/env python3
import os

os.chdir('/storage/brno3-cerit/home/kika/blasto_comparative/maker/')
gff = open('Omod_genome_final_masked.all.gff')

with open('Omod_genome_final_masked.all_upd.gff', 'w') as out:
	for line in gff:
		if '_AED' not in line:
			out.write(line)
		else:
			aed = float(line.split('\t')[-1].split(';')[3].split('=')[1])
			if aed > 0.25:
				pass
			else:
				out.write(line)
