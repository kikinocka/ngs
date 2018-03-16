#!/usr/bin/python3
import os
from Bio import SeqIO
from Bio.Blast import NCBIXML

os.chdir('/home/kika/MEGAsync/diplonema_mt/1601/transcripts/y6/')
xml = open('y6_blast.xml')
blast_records = NCBIXML.parse(xml)

coordinates = {}
for record in blast_records:
	try:
		best_hit = record.alignments[0].hsps[0]
		qstart = best_hit.query_start-1
		qend = best_hit.query_end
		frame = best_hit.frame[1]
		if best_hit.sbjct_start < best_hit.sbjct_end:
			sstart = best_hit.sbjct_start
			send = best_hit.sbjct_end
		else:
			sstart = best_hit.sbjct_end
			send = best_hit.sbjct_start
		if sstart in coordinates:
			pass
		else:
			coordinates[sstart] = [record.query[4:], qstart, qend, frame]
	except:
		print(record.query + '\tno hit found')

c = 0
with open('y6_modules.txt', 'w') as modules:
	for item in sorted(coordinates.items()):
		c += 1
		for seq in SeqIO.parse('y6_contigs.txt', 'fasta'):
			if item[1][0] in seq.name:
				if item[1][3] > 0:
					modules.write('>m{}\n{}\n'.format(c, seq.seq[item[1][1]:item[1][2]]))
				else:
					modules.write('>m{}\n{}\n'.format(c, seq.seq[item[1][1]:item[1][2]].reverse_complement()))