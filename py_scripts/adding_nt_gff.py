#!/usr/bin/python3
infile = open('/home/kika/Dropbox/blastocrithidia/datasets/aa_ref_for_blasto/p57_DNA_aa_ref_for_bla_with_stops.gff', 'r')
output = open('/home/kika/Dropbox/blastocrithidia/datasets/aa_ref_for_blasto/p57_DNA_aa_ref_for_bla_nt_after_stop.gff', 'w')

output.write('{}\t{}\n'.format('##gff-version', '3'))

infile.readline()
for row in infile:
	split_row = row.split('\t')
	name = split_row[0]
	attribute = split_row[1]
	feature = split_row[2]
	start = int(split_row[3])
	stop = int(split_row[4])
	score = split_row[5]
	strand = split_row[6]
	codon = split_row[7]
	description = split_row[8]

	stop = stop + 1
	new_row = '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(name,attribute,feature,start,stop,score,strand,codon,description)		
	output.write(new_row)
output.close()