#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Tat_system/in'
db = '/home/kika/programs/blast-2.5.0+/bin/el_merged.fasta'
out = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Tat_system/out'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)