#!/usr/bin/env python3
from Bio import SeqIO
from Bio.Blast import NCBIXML

genome = SeqIO.parse('/home/kika/MEGAsync/diplonema_mt/1604/genome_assembly/1604_DNA_scaffolds.fasta', 'fasta')
contigs = SeqIO.parse('/home/kika/MEGAsync/diplonema_mt/1604/chromosome_classes/1604_DNA_contigs.fasta', 'fasta')
result_handle = open('/home/kika/MEGAsync/diplonema_mt/1604/additional_contigs/ends_blast.xml')
blast_records = NCBIXML.parse(result_handle)
out = open('/home/kika/MEGAsync/diplonema_mt/1604/additional_contigs/additional_contigs.fa', 'w')

cont_names = []
for contig in contigs:
	cont_names.append(contig.name.replace('_(reversed)', ''))

print('Searching BLAST results.')
new_contigs = set()
for record in blast_records:
	for aln in record.alignments:
		if aln.hit_id in cont_names:
			pass
		else:
			length = int(aln.hit_id.split('_')[3])
			coverage = float(aln.hit_id.split('_')[5])
			if (length > 200) and (coverage > 100):
				for hsp in aln.hsps:
					if hsp.expect < 0.0001:
						new_contigs.add(aln.hit_id)

print('Searching for additional contigs in the genome.')
for contig in genome:
	if contig.name in new_contigs:
		out.write('>{}\n{}\n'.format(contig.description, contig.seq))

out.close()