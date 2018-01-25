#!/usr/bin/python3
import os
from Bio import SeqIO
from collections import OrderedDict

os.chdir('/home/kika/paratrypanosoma/')
in_gbk = SeqIO.parse('Paratrypanosoma_prot_annottions_Blast2GO_final_repaired.gbk', 'gb')
gff = open('result_renamed.gff')
gbk = open('paratryp_renamed.gbk', 'w')

rows = gff.readlines()
names = OrderedDict()
for row in rows:
	old = row.split('\t')[8].split('ID=')[1]
	new = row.split('\t')[9][:-1]
	names[old] = new

for record in in_gbk:
	if record.id in names.keys():
		length = str(record.features[0].location).split(':')[1].split(']')[0]
		beg = int(str(record.features[0].location).split(':')[0].replace('[', '')) + 1
		if len(length) == 4:
			line = 'LOCUS       {}      {} aa            linear   UNA \n'.format(names[record.id], length)
		elif len(length) == 3:
			line = 'LOCUS       {}       {} aa            linear   UNA \n'.format(names[record.id], length)
		elif len(length) == 2:
			line = 'LOCUS       {}        {} aa            linear   UNA \n'.format(names[record.id], length)
		gbk.write(line)
		gbk.write('FEATURES             Location/Qualifiers\n')
		gbk.write('     CDS             {}..{}\n'.format(beg, length))
		gbk.write('                     /source=Blast2GO\n')
		gbk.write('                     /ID={}\n'.format(names[record.id]))
		if 'Description' in record.features[0].qualifiers.keys():
			desc = str(record.features[0].qualifiers['Description']).replace('[\'', '').replace('\']', '')
			gbk.write('                     /Description="{}"\n'.format(desc))
		else:
			pass
		if 'Ontology_term' in record.features[0].qualifiers.keys():
			ont_term = str(record.features[0].qualifiers['Ontology_term']).replace('[\'', '').replace('\']', '')
			gbk.write('                     /Ontology_term="{}"\n'.format(ont_term))
		else:
			pass
		if 'Ontology_id' in record.features[0].qualifiers.keys():
			ont_id = str(record.features[0].qualifiers['Ontology_id']).replace('[\'', '').replace('\']', '')
			gbk.write('                     /Ontology_id="{}"\n'.format(ont_id))
		else:
			pass
		gbk.write('ORIGIN\n')
		c = 10
		parts = []
		new_seq = str()
		for i in range(0, len(record.seq), 10):
			part = str(record.seq[i:c]) + ' '
			c += 10
			new_seq += part
		a = 1
		x = 66
		for i in range(0, len(new_seq), 66):
			part = new_seq[i:x]
			x += 66
			if a == 1:
				gbk.write('        {} {}\n'.format(a, part))
			elif a == 61:
				gbk.write('       {} {}\n'.format(a, part))
			elif a >= 121 and a < 1021:
				gbk.write('      {} {}\n'.format(a, part))
			elif a >= 1021:
				gbk.write('     {} {}\n'.format(a, part))
			a += 60
		gbk.write('//\n')
gbk.close()
	

# aa_seqs = OrderedDict()
# for seq in in_aa:
# 	if 'CDS CDS' in seq.description:
# 		desc = 'CDS_' + seq.description.split(' ')[4].replace(':', '_')
# 		after = (seq.description.split(' ')[2] + ' ' + seq.description.split(' ')[3] + ' ' + 
# 			seq.description.split(' ')[4] + ' ' + seq.description.split(' ')[5] + ' ' + 
# 			seq.description.split(' ')[6])
# 		aa_seqs[desc] = (after, str(seq.seq))
# 	elif 'CDS:' in seq.description:
# 		if 'complement' in seq.description:
# 			desc = 'CDS_' + seq.description.split(')')[0].split('(')[1].replace('..', '_')
# 			after = seq.description.split(')')[1]
# 			aa_seqs[desc] = (after, str(seq.seq))
# 		else:
# 			desc = seq.description.split(' ')[0].replace(':', '_').replace('..', '_')
# 			after = (seq.description.split(' ')[1] + ' ' + seq.description.split(' ')[2] + ' ' + 
# 				seq.description.split(' ')[3] + ' ' + seq.description.split(' ')[4] + ' ' +
# 				seq.description.split(' ')[5])
# 			aa_seqs[desc] = (after, str(seq.seq))
# 	elif 'g' in seq.description:
# 		desc = seq.description.split(' ')[0]
# 		after = (seq.description.split(' ')[1] + ' ' + seq.description.split(' ')[2] + ' ' + 
# 			seq.description.split(' ')[3] + ' ' + seq.description.split(' ')[4] + ' ' +
# 			seq.description.split(' ')[5])
# 		aa_seqs[desc] = (after, str(seq.seq))
# 	else:
# 		desc = 'CDS_' + seq.description.split(' ')[2].replace(':', '_')
# 		after = (seq.description.split(' ')[0] + ' ' + seq.description.split(' ')[1] + ' ' + 
# 			seq.description.split(' ')[2] + ' ' + seq.description.split(' ')[3] + ' ' + 
# 			seq.description.split(' ')[4])
# 		aa_seqs[desc] = (after, str(seq.seq))