#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/SUF_system/SufS1_assembly/in'
one = 'Contig6985'
positions = '13326-14500'
strand = 'plus'
db = '/home/kika/programs/blast-2.5.0+/bin/el_reads_new.fa'
out = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/SUF_system/SufS1_assembly/reads.txt'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
# subprocess.call('blastdbcmd -entry {} -db {} -out {} -range={} -strand={}'.format(one, db, out, positions, strand), 
# 	shell=True)
