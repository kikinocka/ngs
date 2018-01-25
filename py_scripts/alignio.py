#!/usr/bin/python3
from Bio import AlignIO
from Bio import SeqIO

alignment = AlignIO.read('/home/kika/alignments/Nup48.marker001.Nup48.fa.aln', 'fasta')

#number of sequences
print(len(alignment))

#number of positions
print(alignment.get_alignment_length())