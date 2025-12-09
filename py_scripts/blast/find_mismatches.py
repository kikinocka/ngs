#!/usr/bin/env python3
import os
from Bio import SeqIO
from Bio.Blast import NCBIXML

os.chdir('/Users/kika/ownCloud/tRNA-aaRS/ATA_to_Met/Trypanosoma_brucei/')
blast_records = NCBIXML.parse(open('Tbruc_CDS.peptides_WT.blast.xml'))
genome = SeqIO.parse('/Users/kika/Downloads/TriTrypDB-68_TbruceiTREU927_AnnotatedCDSs.fasta', 'fasta')
output = 'Tbruc_WT_mismatches_full.tsv'

contig_dir = {}
for record in blast_records:
	try:
		# print(record.query)
		best_hit = record.alignments[0].hsps[0]
		if '+' in best_hit.match:
			# print(best_hit.query)
			# print(best_hit.match)
			# print(best_hit.sbjct)
			plus_positions = [ind for ind, ch in enumerate(best_hit.match) if ch == '+']
			contig_dir[record.query] = [record.alignments[0].hit_id, best_hit.frame[1], 
										best_hit.sbjct_start, best_hit.sbjct_end]

			for position in plus_positions:
				# print(position)
				# print(best_hit.query_start)
				query_plus = best_hit.query[position]
				sbjct_plus = best_hit.sbjct[position]
				change = '{}->{}'.format(sbjct_plus, query_plus)
				changes = [position, change]
				contig_dir[record.query].append(changes)
		else:
			pass
		# print('--------------------------')
	except:
		pass
# print(contig_dir)
print('Reading blast output done!')

# contig_dir[query name] = [subject name, frame, subject start, subject end, [+ position, change], [+ position, change], ...]
# sequence_18491 ['Tb927.1.1120:mRNA', 1, 1018, 1107, [1, 'I->M'], ...]
# sequence_4879: ['Tb11.v5.0669.1', -1, 337, 426, [22, 'I->M']],

with open(output, 'w') as result:
	result.write('peptide\tcontig\trange\tchange\tcodon\n')
	for seq in genome:
		for key, value in contig_dir.items():
			# print(key, value[0])
			if value[0] == seq.name:
				if value[1] >= 0:
					for v in value[4:]:
						start = value[2] + 3*v[0]
						end = start + 2
						condon = seq.seq[start-1:end]
						result.write('{}\t{}\t{}-{}\t{}\t{}\n'.format(key, value[0], start, end, v[1], condon))
				else:
					for v in value[4:]:
						start = value[3] - 3*v[0] - 2
						end = start + 2
						condon = seq.seq[start-1:end].reverse_complement()
						result.write('{}\t{}\t{}-{}\t{}\t{}\n'.format(key, value[0], end, start, v[1], condon))

print('Processing results done!')
