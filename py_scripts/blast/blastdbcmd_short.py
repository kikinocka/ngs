#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/diplonema_mt/1618/transcripts/cox3/in'
db = '/home/kika/programs/blast-2.5.0+/bin/1618_DNA_scaffolds_filtered.fasta'
out = '/home/kika/MEGAsync/diplonema_mt/1618/transcripts/cox3/cox3_hits.txt'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)