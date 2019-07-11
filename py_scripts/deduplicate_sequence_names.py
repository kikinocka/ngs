#!/usr/bin/env python3
import os
from Bio import SeqIO
from collections import OrderedDict
from collections import defaultdict

os.chdir('/home/kika/MEGAsync/diplonema_paramylon/glucanase/')
infile = SeqIO.parse('glucanase_trimal_0.5.aln', 'fasta')
output1 = open('glucanase_trimal_0.5_dedupl.aln', 'w')
output2 = open('glucanase_trimal_0.5_dupl_names.txt', 'w')

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