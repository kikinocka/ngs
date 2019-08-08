#!/usr/bin/env python3
import subprocess

file = '/home/kika/ownCloud/lmex_mutants/eep_ko/in'
one = 'NODE_561_length_10236_cov_106.963874'
positions = '43693-47247'
strand = 'plus'
db = '/home/kika/programs/blast-2.5.0+/bin/eep_k02_pop1_scaffolds.fa'
out = '/home/kika/ownCloud/lmex_mutants/eep_ko/out'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
# subprocess.call('blastdbcmd -entry {} -db {} -out {} -strand={}'.format(one, db, out, strand), shell=True)

# -range={} 
# positions, 