#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/blasto_project/orthofinder/sg_ogs/ins/in'
one = 'NODE_295_length_22397_cov_76.2802'
positions = '13326-14500'
strand = 'plus'
db = '/home/kika/programs/blast-2.5.0+/bin/p57_DNA_scaffolds.fa'
out = '/home/kika/MEGAsync/blasto_project/genes/oxidative_stress/out'

# subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
subprocess.call('blastdbcmd -entry {} -db {} -out {} -range={} -strand={}'.format(one, db, out, positions, strand), 
	shell=True)