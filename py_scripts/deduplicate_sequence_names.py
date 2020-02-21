#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import OrderedDict
from collections import defaultdict

os.chdir('/storage/brno3-cerit/home/kika/nr_blast/')
infile = SeqIO.parse('nr.fa', 'fasta')
output1 = open('nr_dedupl.fa', 'w')
output2 = open('nr_dupl_names.txt', 'w')

multiplications = defaultdict(list)
seq_dict = OrderedDict()
for sequence in infile:
	multiplications[sequence.name].append(sequence.seq)
	if sequence.name not in seq_dict:
		seq_dict[sequence.description] = sequence.seq

for key, value in seq_dict.items():
	output1.write('>{}\n{}\n'.format(key, value))

for key, value in multiplications.items():
    if len(value) > 1:
        output2.write('{}\n'.format(str(key)))

output1.close()
output2.close()