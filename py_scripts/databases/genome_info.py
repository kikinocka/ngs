#!/usr/bin/env python3

species = open('/home/kika/MEGAsync/blasto_project/ku_story/species_NOG.txt')
genome_table = open('/home/kika/MEGAsync/eukaryotes.csv')
lines = genome_table.readlines()

with open('/home/kika/MEGAsync/blasto_project/ku_story/species_NOG_genomes2.tsv', 'w') as out:
	out.write('Species\tGenome size (Mb)\tGC content (%)\n')
	for sp in species:
		for line in lines:
			name = line.split(',')[0].replace('"', '')
			genome = line.split(',')[7]
			gc = line.split(',')[8]
			if sp[:-1] in name:
				print(name)
				out.write('{}\t{}\t{}\n'.format(name, genome, gc))
