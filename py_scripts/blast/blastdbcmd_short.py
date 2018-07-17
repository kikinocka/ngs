#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/SUF_system/SufS1_assembly/in'
one = 'NODE_702_length_7425_cov_105.491'
positions = '1350-2350'
strand = 'plus'
db = '/home/kika/programs/blast-2.5.0+/bin/jaculum_scaffolds_transc.fasta'
out = '/home/kika/MEGAsync/blasto_project/genes/repair/more_from_paper/jac_LmjF.25.1330_hit.txt'

# subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
subprocess.call('blastdbcmd -entry {} -db {} -out {} -strand={}'.format(one, db, out, strand), 
	shell=True)

# -range={} 
# positions, 