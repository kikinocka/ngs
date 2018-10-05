#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/SUF_system/SufS1_assembly/in'
one = 'NODE_10540_length_1053_cov_594.384852'
positions = '1350-2350'
strand = 'minus'
db = '/home/kika/programs/blast-2.5.0+/bin/pelomyxa_p1.fa'
out = '/home/kika/MEGAsync/pelomyxa/ssu_search/p1_ssu2.fa'

# subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
subprocess.call('blastdbcmd -entry {} -db {} -out {} -strand={}'.format(one, db, out, strand), 
	shell=True)

# -range={} 
# positions, 