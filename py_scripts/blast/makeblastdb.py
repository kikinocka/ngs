#!/usr/bin/python3
import subprocess

db = '/home/kika/MEGAsync/Data/kinetoplastids/cther_Trinity_job_11485672.fasta'
dbtype = 'nucl'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
