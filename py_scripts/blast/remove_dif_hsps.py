#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/ownCloud/pelomyxa/augustus_training_set/')
errorf = open('pelo_trinity_mbal_errors.txt')
prot = SeqIO.parse('pelo_trinity_mbal_aa.fa', 'fasta')
nucl = SeqIO.parse('pelo_trinity_mbal_nt.fa', 'fasta')
prot_upd = open('pelo_trinity_mbal_aa_upd.fa', 'w')
nucl_upd = open('pelo_trinity_mbal_nt_upd.fa', 'w')

def remove_dif_hsps(file, errors, out):
	for seq in file:
		if seq.name.split('__')[1] in errors:
			pass
		else:
			out.write('>{}\n{}\n'.format(seq.name, seq.seq))

errors = set()
for line in errorf:
	if 'hsps frames do not correspond' in line:
		errors.add(line.split(' ')[0])

remove_dif_hsps(prot, errors, prot_upd)
remove_dif_hsps(nucl, errors, nucl_upd)
