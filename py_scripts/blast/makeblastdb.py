#!/usr/bin/env python3
import subprocess

db = '/Dcko/ownCloud/blastocrithidia/genome_assembly/blastdb/p57_polished.fa'
dbtype = 'nucl'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
