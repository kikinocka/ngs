#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/diplonema/pyruvate_metabolism/PDH/aceE/')
transcriptome = SeqIO.parse('aceE_ref.deduplicated.fa', 'fasta')
result = open('aceE_ref.deduplicated_longer900.fa', 'w')

all_cont = 0
long_cont = 0
for contig in transcriptome:
	# print(contig.description)
	all_cont += 1
	if len(contig.seq) < 200:
		pass
	else:
		long_cont += 1
		result.write('>{}\n{}\n'.format(contig.description, contig.seq))

print('Count of contigs in input: {}'.format(all_cont))
print('Count of contigs longer than 200nt: {}'.format(long_cont))
