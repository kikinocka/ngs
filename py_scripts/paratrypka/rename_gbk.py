#!/usr/bin/python3
import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
from Bio.SeqFeature import SeqFeature, FeatureLocation
from collections import OrderedDict

os.chdir('/home/kika/paratrypanosoma/20180208_new/')
in_gbk = SeqIO.parse('Paratrypanosoma_prot_annottions_Blast2GO_final_repaired.gbk', 'gb')
gff = open('Pconfusum_genes_repaired.gff')
gbk = open('paratryp_renamed.gbk', 'w')
err = open('errors.txt', 'w')

names = OrderedDict()
for row in gff:
	try:
		old = row.split('\t')[8].split('Note=')[1][:-1]
		new = row.split('\t')[8].split('=')[1].split(';')[0]
		names[old] = new
	except:
		pass

for record in in_gbk:
	if record.id in names.keys():
		sequence_object = Seq(str(record.seq), IUPAC.protein)
		new = SeqRecord(sequence_object,
				id = names[record.id],
				name = names[record.id])
		feature = SeqFeature(
					FeatureLocation(start = record.features[0].location.start, 
									end = record.features[0].location.end), 
					qualifiers = record.features[0].qualifiers,
					type = 'CDS')
		feature.qualifiers['ID'] = names[record.id]
		new.features.append(feature)
		SeqIO.write(new, gbk, 'genbank')
	else:
		err.write('{}\n'.format(record.id))

gbk.close()
err.close()