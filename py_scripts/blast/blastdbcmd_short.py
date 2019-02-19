#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Phylloquinone/assembly_MenDHC/input.fasta'
one = 'TRINITY_DN2240_c0_g1_i2'
positions = '43693-47247'
strand = 'plus'
db = '/home/kika/programs/blast-2.5.0+/bin/el_reads_new.fa'
out = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Phylloquinone/assembly_MenDHC/out.txt'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
# subprocess.call('blastdbcmd -entry {} -db {} -out {} -strand={}'.format(one, db, out, strand), 
# 	shell=True)

# -range={} 
# positions, 