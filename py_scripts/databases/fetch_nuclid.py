#!/usr/bin/env python3
import os
import re
from Bio import Seq,SeqIO,Entrez

#courtesy of github.com/morpholino

#http://etetoolkit.org/docs/2.3/tutorial/tutorial_ncbitaxonomy.html
Entrez.email = 'kika.zahonova@gmail.com'

os.chdir('/Users/kika/ownCloud/diplonema/pyruvate_metabolism/PDH/aceE')
acc_file = 'aceE.acc'
text_out = 'aceE_nucl2.txt'
fasta_out = 'aceE_nucl2.fa'

def join_nucl(accession, ranges):
	nucl = Entrez.efetch(db='nucleotide', id=accession, rettype='fasta', retmode='text')
	nucl_record = SeqIO.read(nucl, 'fasta')
	acc = nucl_record.name
	#desc = nucl_record.description.replace(acc + " ", "")
	sequence = nucl_record.seq
	subseq = sequence[:0]
	for start,end in ranges:
		subseq += sequence[start-1:end]
	print("SEQ retrieved:", acc)

	return subseq


def get_nucl(accession, start, end):
	nucl = Entrez.efetch(db='nucleotide', id=accession, rettype='fasta', retmode='text')
	nucl_record = SeqIO.read(nucl, 'fasta')
	acc = nucl_record.name
	#desc = nucl_record.description.replace(acc + " ", "")
	sequence = nucl_record.seq[start-1:end]
	print("SEQ retrieved:", acc)

	return sequence


def get_nucl_from_aa(accession):
	#explanation of db structure:
	"""nucl = Entrez.einfo(db='nucleotide')
	record = Entrez.read(nucl)
	record.keys()
	record["DbInfo"]"""

	nucl = Entrez.efetch(db='protein', id=accession, rettype='gb', retmode='xml')
	record = Entrez.read(nucl)[0] #only one record is expected
	#nucl_sequence = record['GBSeq_sequence']
	features = record['GBSeq_feature-table']
	try:
		features = [x for x in features if x['GBFeature_key'] == 'CDS'][0] #only one CDS will be extracted
	except IndexError:
		print("features do not contain CDS category!")
		print(accession, features)
		return "N/A", "N/A"
	#orgn = nucl_record.annotations['organism']
	nucl_locus, nucl_coord = "N/A", "N/A"
	for item in features['GBFeature_quals']:
		#does not work with multiple ranges!
		if item['GBQualifier_name'] == 'locus_tag':
			nucl_locus = item['GBQualifier_value']
		if item['GBQualifier_name'] == 'coded_by':
			nucl_coord = item['GBQualifier_value']
			break
	print("SEQ retrieved:", accession)

	return nucl_coord, nucl_locus

def main():
	coord_re = r'(\w+\.\d+):[<]*(\d+)\.\.(\d+)'
	stops = {'TAA', 'TAG', 'TGA'}
	with open(acc_file) as f,\
		open(text_out, "wt") as result,\
		open(fasta_out, "wt") as fastaout:
		#result.write("protID\tcoded_by\tlocus_id\n")
		for l in f:
			l = l.strip()
			nucl_coord, nucl_locus = get_nucl_from_aa(l)
			result.write("{}\t{}\t{}\n".format(l, nucl_coord, nucl_locus))
			if nucl_coord != "N/A":
				if "join(" in nucl_coord:
					#print("multiple ranges!")
					accessions = [hit[0] for hit in re.findall(coord_re, nucl_coord)]
					if len(set(accessions)) >1:
						print("multiple target sequences!")
						continue
					else:
						accession = accessions[0]
					ranges = [(int(hit[1]), int(hit[2])) for hit in re.findall(coord_re, nucl_coord)]
					start, end = ranges[0][0], ranges[-1][-1]
					locus_seq = join_nucl(accession, ranges)
				else:
					locus_data = re.search(coord_re, nucl_coord)
					accession = locus_data.group(1)
					start, end = int(locus_data.group(2)), int(locus_data.group(3))
					locus_seq = get_nucl(accession, start, end)
				if nucl_coord.startswith("complement("):
					locus_seq = locus_seq.reverse_complement()
				if locus_seq[-3:] in stops:
					locus_seq = locus_seq[:-3]
					end = end-3
				fastaout.write(">{} {}:{}-{}\n{}\n".format(l, accession, start, end, locus_seq))

if __name__ == '__main__':
	main()