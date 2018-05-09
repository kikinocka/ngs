#!/usr/bin/python3
from Bio import AlignIO
from Bio import SeqIO

alignment = AlignIO.read('/home/kika/blasto_project/apicomplexans/ENOG4101NYF.marker001.apiNOG.ENOG4101NYF.meta_raw.fa.aln', 'fasta')

#number of sequences
print(len(alignment))

#number of positions
print(alignment.get_alignment_length())