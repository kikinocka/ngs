#!/usr/bin/env python3
import subprocess

file = '/home/kika/ownCloud/pelomyxa/mito_proteins/pyruvate_metabolism/in'
one = 'NODE_38_length_30771_cov_87.5178'
positions = '43693-47247'
strand = 'plus'
db = '/home/kika/programs/blast-2.5.0+/bin/pelo_trinity.fa'
out = '/home/kika/ownCloud/pelomyxa/mito_proteins/pyruvate_metabolism/pfl_hits.fa'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
# subprocess.call('blastdbcmd -entry {} -db {} -out {} -strand={}'.format(one, db, out, strand), 
# 	shell=True)

# -range={} 
# positions, 