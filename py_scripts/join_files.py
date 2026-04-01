import os
from Bio import SeqIO


# os.chdir('/home/kika/Dropbox/blasto_project/blastocrithidia/genes/cv_subunits/p57/')
# files = os.listdir()

# for file in files:
# 	if '_aa.txt' in file:
# 		gene = file.split('_')[1]
# 		f = SeqIO.parse(file, 'fasta')
# 	out = '/home/kika/Dropbox/blasto_project/blastocrithidia/genes/cv_subunits/triat/p57_' + gene + '.txt'
# 	for protein in f:
# 		with open(out, 'w') as result:
# 			result.write('>{}_{}\n{}\n'.format(gene, protein.name, protein.seq))

# os.chdir('/home/kika/Dropbox/blasto_project/blastocrithidia/genes/cv_subunits/triat/')
# os.system('cat *.txt > p57_input.txt')


os.chdir('/Users/kika/data/eukprot_v3/')
fastas = [x for x in os.listdir() if x.endswith('.fasta')]
table = open('EukProt_included_data_sets.v03.2021_11_22.tsv')
out_tax = 'eukprot_v3.taxidmapping'
out_db = 'eukprot_v3.faa'

datadict = {}
for line in table:
	eukprotID = line.split('\t')[0]
	taxID = line.split('\t')[1]
	organism = line.split('\t')[2]
	# print(organism)
	full_name = eukprotID + '_' + organism
	datadict[full_name] = taxID

with open(out_tax, 'w') as out, open(out_db, 'w') as out_eukprot:
	for fasta in fastas:
		print(fasta)
		for seq in SeqIO.parse(fasta, 'fasta'):
			name = '_'.join(seq.name.split('_')[:-1])
			if name in datadict:
				out.write('{}\t{}\n'.format(seq.name, datadict[name]))
				out_eukprot.write('>{}\n{}\n'.format(seq.name, seq.seq))
			else:
				print(name)

