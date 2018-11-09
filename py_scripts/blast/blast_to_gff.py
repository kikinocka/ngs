#!/usr/bin/env python3
infile = open('/home/kika/MEGAsync/diplonema_mt/1608/transcripts/gff/all_modules_best_blast.tsv')
output = open('/home/kika/MEGAsync/diplonema_mt/1608/transcripts/gff/all.gff', 'w')

output.write('{}\t{}\n'.format('##gff-version', '3'))


for row in infile:
	try:
		split_row = row.split('\t')
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

		note = 'Name=' + sseqid + ';ID=' + qseqid.replace('_', '-')

		output.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(sseqid, 'blast', 'exon', int(sstart), 
			int(new_send), '.', strand, '.', note))
	except:
		pass
output.close()