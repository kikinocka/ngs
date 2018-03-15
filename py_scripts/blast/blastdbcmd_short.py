#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/diplonema_mt/1604/transcripts/nad4/in'
one = 'NODE_379_length_14747_cov_61.7013'
positions = '6786-8294'
strand = 'minus'
db = '/home/kika/programs/blast-2.5.0+/bin/1604_DNA_scaffolds_filtered.fasta'
out = '/home/kika/MEGAsync/diplonema_mt/1604/transcripts/nad4/m5_hit.txt'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
# subprocess.call('blastdbcmd -entry {} -db {} -out {} -range={} -strand={}'.format(one, db, out, positions, strand), 
# 	shell=True)