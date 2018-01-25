import sys
import os
from Bio.Blast import NCBIWWW, NCBIXML, NCBIStandalone
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO
import re
from Bio.Alphabet import generic_dna

# XML formatted blast output

blastout = sys.argv[1]

#QueryFile (FASTA)
queryfile = open(sys.argv[2])
# FASTA file used to make blast db (organism's transcriptome for example)
FASTAFILE = sys.argv[3]
evaluecutoff = float(sys.argv[4])

result_handle = open(blastout)
blast_records = NCBIXML.parse(result_handle)

#QUERY File parsing:

QUERYDICT = {} 

def getseq(AmoebaHIT):
	SEQUENCE = ''
	for contig in SeqIO.parse(FASTAFILE, "fasta"):

		if AmoebaHIT in contig.description:
			print(AmoebaHIT)
			SEQUENCE = str(contig.seq)
	return SEQUENCE

for PhyloGene in SeqIO.parse(queryfile, "fasta"):
	
	QUERYY = str(PhyloGene.description).strip(";")
	QUERYDICT[QUERYY] = []
	#print QUERYDICT
	
def get_translation(SEQUENCE, frame):
	my_seq = Seq(SEQUENCE, generic_dna)
	if frame == 1:
		protein = my_seq.translate()
		return protein
	elif frame == 2:
		protein = my_seq[1:].translate()
		return protein
	elif frame == 3:
		protein = my_seq[2:].translate()
		return protein
	elif frame == -1:
		revcom = my_seq.reverse_complement()
		protein = revcom.translate()
		return protein
	elif frame == -2:
		revcom = my_seq.reverse_complement()
		protein = revcom[1:].translate()
		return protein
	elif frame == -3:
		revcom = my_seq.reverse_complement()
		protein = revcom[2:].translate()
		return protein

"""
def find_protein(translation, subject):
	x =  find_protein1(translation, subject)
	if len(x) <= len(translation)/3:
		return find_protein2(translation, subject)
	else:
		return x
"""



def find_protein(translation, subject):
	print(translation)
	print(subject)
	pattern_start = translation.find(subject)
	backward = 1
	forward = 1
	true_start = 0
	while translation[pattern_start - backward] != '*':
		backward += 1
		if backward == pattern_start:
			if translation.find('*') == 0:
				start = translation.find('M')
				true_start = 1
			else:
				start = 0
			break
	else:
		if translation.find(subject) == 0:
			start = translation.find('M')
			true_start = 1
		else:
			stop_codon = pattern_start - backward
			start = (translation[stop_codon:]).find('M') + stop_codon
			true_start = 1
	while translation[pattern_start + len(subject) + forward] != '*':
		forward += 1
		if pattern_start + len(subject) + forward == len(translation):
			stop = len(translation)
			break
	else:
		stop = pattern_start + len(subject) + forward + 1
	if true_start == 0:
		return translation[start:stop]
	else:
		return '^{}'.format(translation[start:stop])
"""
def find_protein2(translation, subject):
	pattern_start = translation.find(subject)
	backward = 1
	forward = 1

	while translation[pattern_start - backward] != '*':
		backward += 1
		if backward == pattern_start:
			start = 0
			break
	else:
		stop_codon = pattern_start - backward
		start = (translation[stop_codon:]).find('M') + stop_codon
	while translation[pattern_start + len(subject) + forward] != '*':
		forward += 1
		if pattern_start + len(subject) + forward == len(translation):
			stop = len(translation)
			break
	else:
		stop = pattern_start + len(subject) + forward + 1
	return (translation[start:stop])
"""

#Go through and read blast hits for each query and write to file
j = 0
for record in blast_records:

	QUERY = (str(record.query)).strip()

	try:

		for i in range(len(record.alignments)):
			HIThandle = record.alignments[i]
			
			
			for j in range(len(HIThandle.hsps)):
				evalue = HIThandle.hsps[j].expect
				x = str(HIThandle.title.split(" ")[1])
				AmoebaLENGTH = str(HIThandle.title.split(" ")[5])
				frame = HIThandle.hsps[j].frame[-1]
				subject_full = HIThandle.hsps[j].sbjct
				subject = subject_full.replace('-','')

				
				if evalue <= evaluecutoff:
					AmoebaHIT = '{} '.format(str(HIThandle.title.split(" ")[1]))
					SEQUENCE = getseq(AmoebaHIT)
					translation = get_translation(SEQUENCE, frame)
					protein = find_protein(translation, subject)
					QUERYDICT[QUERY].append("%s:%s:%s:%s:%s" % (AmoebaHIT, AmoebaLENGTH, evalue, SEQUENCE, protein))

		
	except IndexError:
		pass
		


outfile = open("%s_parsed.csv" % (blastout), "w")
header = "PhyloProtein Query: AMOEBA HIT CONTIG: AMOEBA LENGTH: evalue\n"
outfile.write(header)

for Query in QUERYDICT:
	HITS = QUERYDICT[Query]
	for HitINFO in HITS:
		outfile.write("%s:%s\n" % (Query,HitINFO))
		

outfile.close()

