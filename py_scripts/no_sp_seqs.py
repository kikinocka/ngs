#!/usr/bin/python3

infile = open('/home/kika/MEGAsync/Publikacie/E. longa plastid/S16.tsv', 'r')
out_fasta = open('/home/kika/MEGAsync/Publikacie/E. longa plastid/no_SP.fasta', 'w')
out_table = open('/home/kika/MEGAsync/Publikacie/E. longa plastid/no_SP.tsv	', 'w')

for line in infile:
	split_line = line.split('\t')
	name = split_line[0]
	
	try:
		SP = split_line[10]
		sequence = split_line[12]
		if SP == 'no SP':
			out_fasta.write('>{}\n{}\n'.format(name, sequence))
			out_table.write('{}\t{}\t{}\t{}\n'.format(name, '-', '-', sequence))
		else:
			print('{}: {}\n'.format(name, SP))
	except:
		pass