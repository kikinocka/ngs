#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/diplonema_mt/1608/transcripts/nad7/in'
db = '/home/kika/programs/blast-2.5.0+/bin/1608_DNA_scaffolds_filtered.fasta'
out = '/home/kika/MEGAsync/diplonema_mt/1608/transcripts/nad7/out'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)