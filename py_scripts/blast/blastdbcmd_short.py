#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/SUF_system/SufS1_assembly/in'
one = 'NODE_1596_length_1921_cov_132.828'
positions = '1350-2350'
strand = 'plus'
db = '/home/kika/programs/blast-2.5.0+/bin/jaculum_scaffolds_transc.fasta'
out = '/home/kika/MEGAsync/blasto_project/ku_story/telomere_maintenance/missing/jac_LmjF.30.3000_hit.txt'

# subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
subprocess.call('blastdbcmd -entry {} -db {} -out {} -strand={}'.format(one, db, out, strand), 
	shell=True)

# -range={} 
# positions, 