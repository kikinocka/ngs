#!/usr/bin/env python3
import subprocess

db = '/Dcko/MEGAsync/Data/EL_RNAseq/NCBI_submission/GGOE01.1.fsa'
dbtype = 'nucl'

subprocess.call('makeblastdb -in {} -dbtype {} -parse_seqids'.format(db, dbtype), shell=True)
