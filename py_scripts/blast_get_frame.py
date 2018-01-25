#!/usr/bin/python3
from Bio.Blast import NCBIXML

result_handle = open('/home/kika/programs/blast-2.5.0+/bin/output.xml')
blast_records = NCBIXML.parse(result_handle)
output = open('/home/kika/programs/blast-2.5.0+/bin/frames.txt', 'w')

for record in blast_records:
	output.write(record.query + '\n')
	for aln in record.alignments:
		for hsp in aln.hsps:
			if hsp.frame[1] == 1:
				output.write(aln.hit_id + '_1\n')
			elif hsp.frame[1] == 2:
				output.write(aln.hit_id + '_2\n')
			elif hsp.frame[1] == 3:
				output.write(aln.hit_id + '_3\n')
			elif hsp.frame[1] == -1:
				output.write(aln.hit_id + '_4\n')
			elif hsp.frame[1] == -2:
				output.write(aln.hit_id + '_5\n')
			elif hsp.frame[1] == -3:
				output.write(aln.hit_id + '_6\n')
			else:
				output.write('no_such_frame')
output.close()