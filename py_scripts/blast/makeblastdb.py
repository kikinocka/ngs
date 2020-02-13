#!/usr/bin/python3
import subprocess

db = '/Dcko/MEGAsync/diplonema/transcriptomes/1608_Trinity.fasta'
dbtype = 'nucl'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
