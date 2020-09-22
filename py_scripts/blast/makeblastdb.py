#!/usr/bin/env python3
import subprocess

db = '/Users/kika/ownCloud/data/stramenopiles/pseudophyllomitus_vesiculosus.fa'
dbtype = 'nucl'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
