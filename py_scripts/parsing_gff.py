#!/usr/bin/python3
infile = open('/home/kika/Dropbox/blastocrithidia/datasets/aa_ref_for_blasto/p57_DNA_aa_ref_for_bla_more_than1.gff', 'r')
output = open('/home/kika/Dropbox/blastocrithidia/datasets/aa_ref_for_blasto/p57_DNA_aa_ref_for_bla_more_than1_with_stops.gff', 'w')

output.write('{}\t{}\n'.format('##gff-version', '3'))

infile.readline()
for row in infile:
	split_row = row.split('\t')
	name = split_row[0]
	attribute = split_row[1]
	feature = split_row[2]
	start = split_row[3]
	stop = split_row[4]
	score = split_row[5]
	strand = split_row[6]
	codon = split_row[7]
	description = split_row[8]

	if feature == 'gene':
		if strand == '+':
			stop = int(stop) + 3
		elif strand == '-':
			if int(start) <= 3:
				start = 1
			else:
				start = int(start) - 3
		else:
			print("error strand")
		new_row = '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(name,attribute,feature,start,stop,score,strand,codon,description)
	else:
		new_row = row
		
	output.write(new_row)
output.close()