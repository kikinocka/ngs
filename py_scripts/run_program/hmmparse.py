#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir("/Users/zoliq/ownCloud/progs/PYTHON/mydata")
"""
prefixes = [x for x in os.listdir() if x.endswith(".ali")]
prefixes = ["PF00134_rp75", "PF02984_rp75"]
for prefix in prefixes:
	os.system("~/.local/bin/hmmer-3.2.1/src/hmmbuild {0}.hmm {0}.ali".format(prefix))
	os.system("~/.local/bin/hmmer-3.2.1/src/hmmsearch -o {0}.result.txt --notextw --tblout {0}.table.txt --cpu 2 {0}.hmm hmmdb.fa".format(prefix, prefix))
"""
#read in seqs from DB fasta only if seqname in results:
files = [x for x in os.listdir() if x.endswith("table.txt")]
alltables = set()
for file in files:
	data = open(file).read().split()
	for item in data:
		alltables.add(item)

seq_d = {}
fastafile = SeqIO.parse("hmmdb.fa", "fasta")
for seq in fastafile:
	if seq.name in alltables:
		seq_d[seq.name] = seq.seq

#filter results and export fasta
multidomain = set()
written = set() #move multidomain, written into the for loop to have domain-specific files
for file in files:
	name = file.replace(".table.txt", "-dbhits.fasta")
	with open(file) as infile, open(name, "w") as result:
		for line in infile:
			if not line.startswith("#"):
				data = line.split()
				seqname = data[0]
				evalue = float(data[4])
				if seqname in written:				
					pass
				elif evalue < 0.01:
					result.write(">{}\n{}\n".format(seqname, seq_d[seqname]))
					written.add(seqname)
					multidomain.add(seqname)
				elif seqname in multidomain: #several domains found in the same seq
					result.write(">{}\n{}\n".format(seqname, seq_d[seqname]))
					written.add(seqname)
				else:
					multidomain.add(seqname)
