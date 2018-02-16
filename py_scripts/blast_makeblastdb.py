#!/usr/bin/python3
import subprocess

db = '/home/kika/programs/blast-2.5.0+/bin/1608_DNA_scaffolds_filtered.fasta'
dbtype = 'nucl'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)