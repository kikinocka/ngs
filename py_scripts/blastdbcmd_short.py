#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/blasto_project/genes/repair/NHEJ/ku_pfam/in'
db = '/home/kika/programs/blast-2.5.0+/bin/jaculum_scaffolds_transc.fasta'
out = '/home/kika/MEGAsync/blasto_project/genes/repair/NHEJ/ku_pfam/jac_hit.txt'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)