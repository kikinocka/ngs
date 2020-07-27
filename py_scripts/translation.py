#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/data/diplonemids_transcriptomes/')
infile = SeqIO.parse('1621_Trinity.fasta', 'fasta')
output = open('1621_translated.fa', 'w')
error = open('1621_errors.fa', 'w')

gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'X', 'TAG':'X',
    'TGC':'C', 'TGT':'C', 'TGA':'X', 'TGG':'W'}

def translation(sequence):
    cut_seq = []
    for i in range(0,len(sequence)-2,3):
        cut_seq.append(sequence[i:i+3])
    aa = []
    for codon in cut_seq:
        if ('N' in codon) or ('W' in codon) or ('S' in codon) or ('M' in codon) or ('K' in codon) or ('R' in codon) or ('Y' in codon):
            aa.append('X')
        else:
            aa.append(gencode[codon])
    return ''.join(aa)

i = 0
for sequence in infile:
    i += 1
    name = sequence.name
    seq = sequence.seq.upper()
    ambiguous = False
    print(name)
    for nucleotide in seq:
        if nucleotide not in 'ATCGNWSMKRY':
            ambiguous = True
    if ambiguous == True:
        error.write('>{}\n{}\n'.format(name, seq))
    else:    
        output.write('>{}_1\n{}\n'.format(name, translation(seq)))
        output.write('>{}_2\n{}\n'.format(name, translation(seq[1:])))
        output.write('>{}_3\n{}\n'.format(name, translation(seq[2:])))
        output.write('>{}_4\n{}\n'.format(name, translation(seq.reverse_complement())))
        output.write('>{}_5\n{}\n'.format(name, translation(seq.reverse_complement()[1:])))
        output.write('>{}_6\n{}\n'.format(name, translation(seq.reverse_complement()[2:])))
    if i%100 == 0:
        print(i)
output.close()
error.close()