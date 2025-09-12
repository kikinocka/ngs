#!/usr/bin/python3
import os
from Bio import SeqIO
import matplotlib.pyplot as plt

os.chdir('/Users/kika/Downloads/')

# Path to your FASTA file
fasta_file = 'HBDM01.1.fsa_nt'

# Get lengths of sequences
lengths = [len(record.seq) for record in SeqIO.parse(fasta_file, 'fasta')]

# Plot histogram
plt.hist(lengths, bins=100, color='pink', edgecolor='grey')
plt.title('Histogram of Sequence Lengths')
plt.xlabel('Sequence Length [nt]')
plt.ylabel('Count')
plt.xlim(0, 8000)
plt.grid(True)
plt.tight_layout()
# plt.show()
plt.savefig('HBDM.seq_len.pdf', dpi=300)
