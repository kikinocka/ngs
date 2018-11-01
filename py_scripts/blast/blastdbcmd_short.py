#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/SUF_system/SufS1_assembly/in'
one = 'TRINITY_DN97191_c0_g1_i1'
positions = '43693-47247'
strand = 'plus'
db = '/home/kika/programs/blast-2.5.0+/bin/bexlh2_strict.fa'
out = '/home/kika/ownCloud/blastocrithidia/ssu_tree/bexlh2_rRNA_contig.fa'

# subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
subprocess.call('blastdbcmd -entry {} -db {} -out {} -strand={}'.format(one, db, out, strand), 
	shell=True)

# -range={} 
# positions, 