#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/SUF_system/SufS1_assembly/in'
one = 'TRINITY_DN17973_c0_g1_i1'
positions = '43693-47247'
strand = 'plus'
db = '/home/kika/programs/blast-2.5.0+/bin/lhes1_PRJNA238835_trinity.fasta'
out = '/home/kika/ownCloud/blastocrithidia/ssu_tree/lehs1_rRNA_contig.fa'

# subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
subprocess.call('blastdbcmd -entry {} -db {} -out {} -strand={}'.format(one, db, out, strand), 
	shell=True)

# -range={} 
# positions, 