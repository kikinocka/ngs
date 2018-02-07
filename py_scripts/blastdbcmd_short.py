#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/blasto_project/genes/repair/more_from_paper/in'
db = '/home/kika/programs/blast-2.5.0+/bin/p57_DNA_scaffolds.fa'
out = '/home/kika/MEGAsync/blasto_project/genes/repair/more_from_paper/out'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)