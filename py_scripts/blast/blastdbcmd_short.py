#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/diplonema_mt/1601/transcripts/y6/in'
one = 'NODE_379_length_14747_cov_61.7013'
positions = '6786-8294'
strand = 'minus'
db = '/home/kika/programs/blast-2.5.0+/bin/1601_DNA_scaffolds.fasta'
out = '/home/kika/MEGAsync/diplonema_mt/1601/transcripts/y6/y6_hits.txt'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
# subprocess.call('blastdbcmd -entry {} -db {} -out {} -range={} -strand={}'.format(one, db, out, positions, strand), 
# 	shell=True)