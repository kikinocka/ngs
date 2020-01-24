#!/usr/bin/python3
import subprocess

db = '/home/kika/MEGAsync/Data/kinetoplastids/TriTrypDB-46_LseymouriATCC30220_AnnotatedCDSs.fasta'
dbtype = 'nucl'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
