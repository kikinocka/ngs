#!/usr/bin/env python3
import subprocess

file = '/home/kika/MEGAsync/Manuscripts/Blasto_Ku70-80/Figures/alignments/in'
one = 'NODE_485_length_9557_cov_106.73'
positions = '43693-47247'
strand = 'plus'
db = '/home/kika/programs/blast-2.5.0+/bin/jaculum_scaffolds_transc.fasta'
out = '/home/kika/MEGAsync/Manuscripts/Blasto_Ku70-80/Figures/alignments/jac_out'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
# subprocess.call('blastdbcmd -entry {} -db {} -out {} -strand={}'.format(one, db, out, strand), shell=True)

# -range={} 
# positions, 