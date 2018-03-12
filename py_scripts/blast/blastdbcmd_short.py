#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/srp/in'
one = 'NODE_379_length_14747_cov_61.7013'
positions = '6786-8294'
strand = 'minus'
db = '/home/kika/programs/blast-2.5.0+/bin/eg_tsa_Yoshida.fsa'
out = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/srp/out'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
# subprocess.call('blastdbcmd -entry {} -db {} -out {} -range={} -strand={}'.format(one, db, out, positions, strand), 
# 	shell=True)