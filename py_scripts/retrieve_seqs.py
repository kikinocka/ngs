import os
from Bio import SeqIO

os.chdir('/storage/brno3-cerit/home/kika/blasto_comparative/blobtools/reports/Bfru_contaminants/')
files = [x for x in os.listdir() if x.endswith('.acc')]
database = '/storage/brno3-cerit/home/kika/blasto_comparative/blobtools/assemblies/Bfru.platanus_rnd2_scaffold.l500.gapcloser.fa'

for accessions in files: 
	print(accessions)
	fname = accessions.split('.acc')[0]
	retrieve = set()

	with open('{}.fa'.format(fname), 'w') as out:
		db = SeqIO.parse(database, 'fasta')

		for line in open(accessions):
			retrieve.add(line[:-1])
		# print(retrieve)
		for seq in db:
			if seq.name.split(';')[0] in retrieve:
				out.write('>{}\n{}\n'.format(seq.description, seq.seq))
				# pass
			else:
				pass
				# out.write('>{}\n{}\n'.format(seq.description, seq.seq))

