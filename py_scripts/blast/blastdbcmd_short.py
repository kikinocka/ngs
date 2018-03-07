#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/sec/secY/in'
db = '/home/kika/programs/blast-2.5.0+/bin/pyramimonas_sp_CCMP2087.nt.fa'
out = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/sec/secY/psp_nt.txt'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)