#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/blasto_project/orthofinder/sg_ogs/ins/in'
one = 'CAMNT_0000668555'
positions = '6786-8294'
strand = 'minus'
db = '/home/kika/programs/blast-2.5.0+/bin/jaculum_scaffolds.fasta'
out = '/home/kika/MEGAsync/blasto_project/orthofinder/sg_ogs/ins/out'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
# subprocess.call('blastdbcmd -entry {} -db {} -out {} -range={} -strand={}'.format(one, db, out, positions, strand), 
# 	shell=True)