#!/usr/bin/env python3
import subprocess

file = '/home/kika/ownCloud/pelomyxa_schiedti/mito_proteins/aa_metabolism/in'
one = 'NODE_846_length_3434_cov_172.242776'
positions = '43693-47247'
strand = 'plus'
db = '/home/kika/programs/blast-2.5.0+/bin/pelo_trinity.fa'
out = '/home/kika/ownCloud/pelomyxa_schiedti/mito_proteins/aa_metabolism/out'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
# subprocess.call('blastdbcmd -entry {} -db {} -out {} -strand={}'.format(one, db, out, strand), shell=True)

# -range={} 
# positions, 