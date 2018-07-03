#!/usr/bin/python3
import os
import re
from Bio import SeqIO

os.chdir('/media/4TB1/blastocrithidia/bexlh/reads/trimmed/')
files = os.listdir()

for file in files:
	if '.fq' in file and '.gz' not in file:
		file_name = file.split('.')[0]
		print(file)
		fw = open('/media/4TB1/blastocrithidia/bexlh/reads/trimmed/' + file_name + '_fw.fq', 'w')
		rev = open('/media/4TB1/blastocrithidia/bexlh/reads/trimmed/' + file_name + '_rev.fq', 'w')
		errors = open('/media/4TB1/blastocrithidia/bexlh/reads/trimmed/' + file_name + '_errors.fq', 'w')
		for read in SeqIO.parse(file, 'fastq'):
			if re.search('SRR\d+.\d+.1 ', read.description):
				print(read.name)
				fw.write(read.format('fastq'))
			elif re.search('SRR\d+.\d+.2 ', read.description):
				print(read.name)
				rev.write(read.format('fastq'))
			else:
				print(read.name)
				errors.write(read.format('fastq'))