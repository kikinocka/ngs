#!/usr/bin/python3
import os
import subprocess

os.chdir('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/pt_division/HMM/')
files = os.listdir()
threads = 4
db = '/home/kika/MEGAsync/Data/Eutreptiella/Eutreptiella_gymnastica_NIES-381.fasta'

for file in files:
	if file.endswith('.hmm'):
		print(file)
		name = file.split('_')[0]
		out = 'nies_' + name + '_search.out'
		subprocess.call('hmmsearch -o {} --cpu {} {} {}'.format(out, threads, file, db), 
			shell=True)
