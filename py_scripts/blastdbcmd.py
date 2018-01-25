#!/usr/bin/python3
import os

db = '/home/kika/programs/blast-2.5.0+/bin/triat_RNA.fasta'
table = open('/home/kika/MEGAsync/blasto_project/genes/replication/triat_repl_RNA_best_blast.xlsx', 'r')
table.readline()

for row in table:
	split_row = row.split('\t')
	qseqid = split_row[0].split('p57_')[1]
	qlen = int(split_row[1])
	sseqid = split_row[2]
	slen = int(split_row[3])
	alen = int(split_row[4])
	evalue = split_row[5]
	pident = int(split_row[6])
	bitscore = float(split_row[7])
	mismatch = int(split_row[8])
	gaps = int(split_row[9])
	qstart = int(split_row[10])
	qend = int(split_row[11])
	sstart = int(split_row[12])
	send = int(split_row[13])
	alen_qlen = float(split_row[14])
	alen_slen = float(split_row[15])
	out = '/home/kika/MEGAsync/blasto_project/genes/replication/triat_' + qseqid + '_nt.txt'

	# if qstart == 1:
	# 	if qend == qlen:
	# 		send = send + 300
	# 	else:
	# 		send = send + 3*(qlen - qend) + 300
	# 	sstart = sstart - 300
	# 	if sstart < 1:
	# 		sstart = 1
	# else:
	# 	if qend == qlen:
	# 		send = send + 300
	# 	else:
	# 		send = send + 3*(qlen - qend) + 300
	# 	sstart = sstart - (3*qstart + 300)
	# 	if sstart < 1:
	# 		sstart = 1
	
	# os.system('blastdbcmd -entry {} -db {} -out {} -range {}-{}'.format(sseqid, db, out, sstart, send))

	os.system('blastdbcmd -entry {} -db {} -out {}'.format(sseqid, db, out))

table.close()