#!/usr/bin/env python3
import subprocess

file = '/home/kika/ownCloud/euglenophytes/pt_proteome/Eut/in'
one = 'NODE_485_length_9557_cov_106.73'
positions = '43693-47247'
strand = 'plus'
db = '/home/kika/programs/blast-2.5.0+/bin/eg_deeg.fa'
out = '/home/kika/ownCloud/euglenophytes/pt_proteome/Eut/EG_photosynthesis_list.fa'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
# subprocess.call('blastdbcmd -entry {} -db {} -out {} -strand={}'.format(one, db, out, strand), shell=True)

# -range={} 
# positions, 