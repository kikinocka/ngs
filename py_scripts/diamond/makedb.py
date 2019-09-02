#!/usr/bin/env python3
import subprocess

fasta = '/home/kika/programs/blast-2.5.0+/bin/CAM_P_0001000.pep.fa'
db = '/home/kika/programs/blast-2.5.0+/bin/CAM_P_0001000.pep.fa.dmnd'

subprocess.call('diamond makedb --in {} --db {}'.format(fasta, db), shell=True)
