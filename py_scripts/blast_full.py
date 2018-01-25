#!/usr/bin/python3
#!!! do not forget to change TABLE, OUT, and parsing of QSEQID in the end of script !!!
import os
import subprocess
from Bio.Blast import NCBIXML

out_blast = open('/home/kika/MEGAsync/blasto_project/genes/c_deaminase/p57_imp_mit/blast.tsv', 'w')
out_best = open('/home/kika/MEGAsync/blasto_project/genes/c_deaminase/p57_imp_mit/best_blast.tsv', 'w')
errors = open('/home/kika/MEGAsync/blasto_project/genes/c_deaminase/p57_imp_mit/errors.txt', 'w')

cmd = 'tblastn'
query = '/home/kika/MEGAsync/blasto_project/genes/c_deaminase/imp_mit_candidates.fa'
db = '/home/kika/programs/blast-2.5.0+/bin/p57_DNA_scaffolds.fa'
output = '/home/kika/MEGAsync/blasto_project/genes/c_deaminase/p57_imp_mit/blast.xml'
evalue = 10
outfmt = 5
word_size = 3
threads = 3

print('starting BLAST')
# os.system('{} -query {} -db {} -out {} -evalue {} -outfmt {} -word_size {}'.format(
# 		cmd, query, db, output, evalue, outfmt, word_size))
subprocess.call('{} -query {} -db {} -out {} -evalue {} -outfmt {} -word_size {} -num_threads {}'.format(
		cmd, query, db, output, evalue, outfmt, word_size, threads), shell=True)
print('BLAST done')

result_handle = open(output)
blast_records = NCBIXML.parse(result_handle)

out_blast.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format('qseqid', 'qlen', 'sseqid', 'slen', 
	'alen', 'evalue', 'pident', 'bitscore', 'mismatch', 'gaps', 'qstart', 'qend', 'sstart', 'send', 'alen_qlen', 
	'alen_slen'))
out_best.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format('qseqid', 'qlen', 'sseqid', 'slen', 
	'alen', 'evalue', 'pident', 'bitscore', 'mismatch', 'gaps', 'qstart', 'qend', 'sstart', 'send', 'alen_qlen', 
	'alen_slen'))

for record in blast_records:
	try:
		best_hit = record.alignments[0].hsps[0]
		mismatches = best_hit.align_length - (best_hit.gaps + best_hit.positives)
		alen_qlen = best_hit.align_length/record.query_length
		alen_slen = best_hit.align_length/record.alignments[0].length
		out_best.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
			record.query, record.query_length, record.alignments[0].hit_id, record.alignments[0].length, 
			best_hit.align_length, best_hit.expect, best_hit.identities, best_hit.bits, mismatches, 
			best_hit.gaps, best_hit.query_start, best_hit.query_end, best_hit.sbjct_start, best_hit.sbjct_end, 
			alen_qlen, alen_slen))
		for aln in record.alignments:
			for hsp in aln.hsps:
				mismatches = hsp.align_length - (hsp.gaps + hsp.positives)
				alen_qlen = hsp.align_length/record.query_length
				alen_slen = hsp.align_length/aln.length
				out_blast.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
					record.query, record.query_length, aln.hit_id, aln.length, hsp.align_length, hsp.expect, 
					hsp.identities, hsp.bits, mismatches, hsp.gaps, hsp.query_start, hsp.query_end, hsp.sbjct_start, 
					hsp.sbjct_end, alen_qlen, alen_slen))
	except:
		out_blast.write('{}\t{}\t{}\n'.format(record.query, record.query_length, '***no hit found***'))
		out_best.write('{}\t{}\t{}\n'.format(record.query, record.query_length, '***no hit found***'))

out_best.close()
out_blast.close()

table = open('/home/kika/MEGAsync/blasto_project/genes/c_deaminase/p57_imp_mit/best_blast.tsv', 'r')
table.readline()

print('sorting hits by evalue')
for row in table:
	split_row = row.split('\t')
	qseqid = split_row[0].split(':')[0]
	qlen = int(split_row[1])
	sseqid = split_row[2]
	try:
		slen = int(split_row[3])
		alen = int(split_row[4])
		evalue = float(split_row[5])
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
		out = '/home/kika/MEGAsync/blasto_project/genes/c_deaminase/p57_imp_mit/' + qseqid + '_nt.txt'

		if evalue < 0.001:
			if qstart == 1:
				if qend == qlen:
					send = send + 300
				else:
					send = send + 3*(qlen - qend) + 300
				sstart = sstart - 300
				if sstart < 1:
					sstart = 1
			else:
				if qend == qlen:
					send = send + 300
				else:
					send = send + 3*(qlen - qend) + 300
				sstart = sstart - (3*qstart + 300)
				if sstart < 1:
					sstart = 1
			b_range = '{}-{}'.format(sstart, send)
			os.system('blastdbcmd -entry {} -db {} -out {} -range {}'.format(sseqid, db, out, b_range))

			# os.system('blastdbcmd -entry {} -db {} -out {}'.format(sseqid, db, out))

		else:
			errors.write('{}: too high evalue ({})\n'. format(qseqid, evalue))

	except:
		errors.write(qseqid + ': no hit found\n')

print('writing hits to files done')

errors.close()
table.close()