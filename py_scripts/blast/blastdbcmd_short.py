#!/usr/bin/env python3
import subprocess

file = '/home/kika/MEGAsync/diplonema/catalase/cther/in'
one = 'NODE_561_length_10236_cov_106.963874'
positions = '43693-47247'
strand = 'plus'
db = '/home/kika/MEGAsync/Data/kinetoplastids/cther_Trinity_job_11485672.fasta'
out = '/home/kika/MEGAsync/diplonema/catalase/cther/cther.nt.fa'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
# subprocess.call('blastdbcmd -entry {} -db {} -out {} -strand={}'.format(one, db, out, strand), shell=True)

# -range={} 
# positions, 