#!/usr/bin/python3
import subprocess

file = '/home/kika/ownCloud/pelomyxa/augustus_training_set/hits'
one = 'NODE_38_length_30771_cov_87.5178'
positions = '43693-47247'
strand = 'plus'
db = '/home/kika/programs/blast-2.5.0+/bin/pelomyxa_final_genome.fa'
out = '/home/kika/ownCloud/pelomyxa/augustus_training_set/hits.fa'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
# subprocess.call('blastdbcmd -entry {} -db {} -out {} -strand={}'.format(one, db, out, strand), 
# 	shell=True)

# -range={} 
# positions, 