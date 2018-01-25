#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/home/kika/tara/test/')
files = os.listdir()

for file in files:
	if '.fasta' in file:
		print(file)
		file_name = file.split('.fasta')[0]
		circular = open('circular_' + file_name + '.fa', 'w')
		rest = open('rest_' + file_name + '.fa', 'w')
		contigs = SeqIO.parse(file, 'fasta')
		for contig in contigs:
			if len(contig.seq) > 3000:
				print(contig.description)
				#search for the beginning repeat at the end of the conting
				for i in range(len(contig.seq)):
					if contig.seq.count(contig.seq[0:i+1]) > 1:
						repeat = str(contig.seq[0:i+1])
					i += 1
				if len(repeat) >= 8 and repeat == contig.seq[-len(repeat):]:
					circular.write('>{}___{}\n{}\n'.format(contig.description, repeat, contig.seq))
				else:
					rest.write('>{}\n{}\n'.format(contig.description, contig.seq))
			else:
				rest.write('>{}\n{}\n'.format(contig.description, contig.seq))
		circular.close()
		rest.close()
	else:
		pass
