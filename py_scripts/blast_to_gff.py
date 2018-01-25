#!/usr/bin/python3
infile = open('/home/kika/Dropbox/blasto_project/blastocrithidia/genome/assembly/p57_DNA_scaffo/blast_reports/p57_RNA_Trinity_bl_report_best.csv', 'r')
output = open('/home/kika/Dropbox/blasto_project/blastocrithidia/transcriptome_trinity/p57_RNA_trinity.gff', 'w')

output.write('{}\t{}\n'.format('##gff-version', '3'))

infile.readline()
for row in infile:
	split_row = row.split(',')
	qseqid = split_row[0]
	qlen = split_row[1]
	sseqid = split_row[2]	
	slen = split_row[3]
	length = split_row[4]	
	evalue = split_row[5]
	pident = split_row[6]
	bitscore = split_row[7]	
	mismatch = split_row[8]	
	gaps = split_row[9]
	qstart = int(split_row[10])
	qend = int(split_row[11])
	sstart = int(split_row[12])
	send = int(split_row[13])
	alen_qlen = float(split_row[14])
	alen_slen = float(split_row[15])

	# if alen_qlen > float(1):
	if sstart > send:
		new_send = sstart
		sstart = send
		strand = '-'
	else:
		sstart = sstart
		new_send = send
		strand = '+'

	note = 'ID=' + qseqid
	output.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(sseqid, 'blast', 'gene', int(sstart), int(new_send), '1', strand, '0', note))
output.close()