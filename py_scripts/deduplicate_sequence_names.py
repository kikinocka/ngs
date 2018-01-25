#!/usr/bin/python3
from Bio import SeqIO
from collections import OrderedDict
from collections import defaultdict

infile = SeqIO.parse('/home/kika/MEGAsync/blasto_project/genes/tRNAs/iqtree/pasta/without_anticodon/trnas_deduplicated_anticodon.fasta', 'fasta')
output1 = open('/home/kika/MEGAsync/blasto_project/genes/tRNAs/iqtree/pasta/without_anticodon/trnas_deduplicated2_anticodon.fasta', 'w')
output2 = open('/home/kika/MEGAsync/blasto_project/genes/tRNAs/iqtree/pasta/without_anticodon/trnas_dupl_names.txt', 'w')

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