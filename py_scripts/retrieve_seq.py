#!/usr/bin/python3
from Bio import SeqIO

infasta = SeqIO.parse('/home/kika/MEGAsync/Chlamydomonas/putative_pt_targeted/targeting_prediction/putative_pt_genes_aa_complete5.fa', 'fasta')
infile = open('/home/kika/MEGAsync/Chlamydomonas/putative_pt_targeted/targeting_prediction/in')
out = open('/home/kika/MEGAsync/Chlamydomonas/putative_pt_targeted/targeting_prediction/pt_predicted.fa', 'w')

retrieve = set()
for line in infile:
	retrieve.add(line[:-1])

for seq in infasta:
	if seq.name.split('_m.')[0] in retrieve:
		out.write('>{}\n{}\n'.format(seq.description, seq.seq))
out.close()