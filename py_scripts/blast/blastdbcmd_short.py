#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/diplonema_mt/1618/transcripts/in'
db = '/home/kika/programs/blast-2.5.0+/bin/1618_DNA_scaffolds_filtered.fasta'
out = '/home/kika/MEGAsync/diplonema_mt/1618/transcripts/y6/y6_hits.txt'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)