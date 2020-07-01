#!/usr/bin/env python3
import subprocess
from Bio.Blast import NCBIXML

cmd = 'tblastn'
task = 'tblastn'
query = '/Users/kika/ownCloud/kinetoplastids/telomeres/Tb927.11.370/synteny.faa'
db = '/Users/kika/ownCloud/data/kinetoplastids/genomes_fasta/TriTrypDB-45_TrangeliSC58_Genome.fasta'
# subject = '/home/kika/MEGAsync/diplonema_mt/1621/transcripts/y8/y8.fasta'
out = '/Users/kika/ownCloud/kinetoplastids/telomeres/Tb927.11.370/tran_synt.blast.xml'
evalue = 1
outfmt = 5
hits = 1
word_size = 3
threads = 5

print('running BLAST')
#query - database
subprocess.call('{} -task {} -query {} -db {} -out {} -evalue {} -outfmt {} -word_size {}  \
	-num_threads {}'.format(
		cmd, task, query, db, out, evalue, outfmt, word_size, threads), shell=True)
# -max_target_seqs {} hits, 

# #query - subject
# subprocess.call('{} -query {} -subject {} -out {} -evalue {} -outfmt {} -word_size {}'.format(
# 		cmd, query, subject, out, evalue, outfmt, word_size), shell=True)

print('BLAST done')
print('writing BLAST results to tables')

result_handle = open(out)
blast_records = NCBIXML.parse(result_handle)
output = open('/Users/kika/ownCloud/kinetoplastids/telomeres/Tb927.11.370/tran_synt.blast.tsv', 'w')
out_best = open('/Users/kika/ownCloud/kinetoplastids/telomeres/Tb927.11.370/tran_synt.best_blast.tsv', 'w')

output.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format('qseqid', 'qlen', 'sseqid', 'sseqdef',
	'slen', 'alen', 'evalue', 'pident', 'bitscore', 'mismatch', 'gaps', 'qstart', 'qend', 'sstart', 'send', 
	'alen_qlen', 'alen_slen'))
out_best.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format('qseqid', 'qlen', 'sseqid', 'sseqdef',
	'slen', 'alen', 'evalue', 'pident', 'bitscore', 'mismatch', 'gaps', 'qstart', 'qend', 'sstart', 'send', 
	'alen_qlen', 'alen_slen'))

for record in blast_records:
	try:
		best_hit = record.alignments[0].hsps[0]
		mismatches = best_hit.align_length - (best_hit.gaps + best_hit.positives)
		alen_qlen = best_hit.align_length/record.query_length
		alen_slen = best_hit.align_length/record.alignments[0].length
		if best_hit.frame[1] > 0:
			# print(record.alignments[0].title)
			out_best.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
				record.query, record.query_length, record.alignments[0].hit_id, record.alignments[0].hit_def, record.alignments[0].length, 
				best_hit.align_length, best_hit.expect, best_hit.identities, best_hit.bits, mismatches, 
				best_hit.gaps, best_hit.query_start, best_hit.query_end, best_hit.sbjct_start, best_hit.sbjct_end, 
				alen_qlen, alen_slen))
		else:
			out_best.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
				record.query, record.query_length, record.alignments[0].hit_id, record.alignments[0].hit_def, record.alignments[0].length, 
				best_hit.align_length, best_hit.expect, best_hit.identities, best_hit.bits, mismatches, 
				best_hit.gaps, best_hit.query_start, best_hit.query_end, best_hit.sbjct_end, best_hit.sbjct_start, 
				alen_qlen, alen_slen))
		for aln in record.alignments:
			for hsp in aln.hsps:
				mismatches = hsp.align_length - (hsp.gaps + hsp.positives)
				alen_qlen = hsp.align_length/record.query_length
				alen_slen = hsp.align_length/aln.length
				if hsp.frame[1] > 0:
					output.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
						record.query, record.query_length, aln.hit_id, aln.hit_def, aln.length, hsp.align_length, hsp.expect, 
						hsp.identities, hsp.bits, mismatches, hsp.gaps, hsp.query_start, hsp.query_end, 
						hsp.sbjct_start, hsp.sbjct_end, alen_qlen, alen_slen))
				else:
					output.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
						record.query, record.query_length, aln.hit_id, aln.hit_def, aln.length, hsp.align_length, hsp.expect, 
						hsp.identities, hsp.bits, mismatches, hsp.gaps, hsp.query_start, hsp.query_end, 
						hsp.sbjct_end, hsp.sbjct_start, alen_qlen, alen_slen))
	except:
		pass
		output.write('{}\t{}\t***no hit found***\n'.format(record.query, record.query_length))
		out_best.write('{}\t{}\t***no hit found***\n'.format(record.query, record.query_length))
out_best.close()
output.close()