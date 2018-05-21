#!/usr/bin/python3
import os
from Bio import SeqIO
from collections import OrderedDict

os.chdir('/home/kika/MEGAsync/Data/EL_RNAseq/20140707_ver._r2013-02-05/')
contamination = open('NCBI_submission/to_trim.txt')
contigs = SeqIO.parse('EL_merged_withoutNs_longer200_without_primers.fsa', 'fasta')
contigs_upd = open('EL_merged_withoutNs_longer200_without_adapters.fsa', 'w')

def get_coordinates(contamination):
	adapters = {}
	for row in contamination:
		if ',' in row.split('\t')[2]:
			for item in row.split('\t')[2].split(','):
				beginning = int(item.split('..')[0])
				end = int(item.split('..')[1])
				whole = [beginning, end]
				if row.split('\t')[0] not in adapters:
					adapters[row.split('\t')[0]] = [whole]
				else:
					adapters[row.split('\t')[0]].append(whole)
		else:
			beginning = int(row.split('\t')[2].split('..')[0])
			end = int(row.split('\t')[2].split('..')[1])
			whole = [beginning, end]
			adapters[row.split('\t')[0]] = [whole]
	return adapters
	# contig name : [[start, end], [start,end]]
	# 				   adaptor1		 adaptor2

adapters = get_coordinates(contamination)
remove = ['Contig1236', 'Contig15838', 'Contig15854', 'Contig15927', 'Contig15942', 'Contig15982', 'Contig16017', 'Contig16041', 'Contig16110', 'Contig16142', 'Contig16218', 'Contig16232', 'Contig16346', 'Contig16378', 'Contig16517', 'Contig16523', 'Contig16538', 'Contig16567', 'Contig16585', 'Contig16605', 'Contig16623', 'Contig16639', 'Contig16651', 'Contig16708', 'Contig16723', 'Contig16949', 'Contig17064', 'Contig17077', 'Contig17175', 'Contig17241', 'Contig17245', 'Contig17353', 'Contig17508', 'Contig17558', 'Contig17687', 'Contig17702', 'Contig17724', 'Contig17725', 'Contig17751', 'Contig183', 'Contig18708', 'Contig18747', 'Contig18759', 'Contig18787', 'Contig18814', 'Contig19270', 'Contig19484', 'Contig19791', 'Contig19844', 'Contig19956', 'Contig201', 'Contig20265', 'Contig20793', 'Contig20830', 'Contig23296', 'Contig292', 'Contig3048', 'Contig37909', 'Contig37950', 'Contig37964', 'Contig38201', 'Contig38273', 'Contig38300', 'Contig38326', 'Contig38328', 'Contig38340', 'Contig38383', 'Contig38398', 'Contig38414', 'Contig38463', 'Contig38473', 'Contig38474', 'Contig38478', 'Contig38479', 'Contig38504', 'Contig38512', 'Contig38530', 'Contig38541', 'Contig38590', 'Contig38615', 'Contig38617', 'Contig38621', 'Contig38645', 'Contig38658', 'Contig38666', 'Contig38690', 'Contig38698', 'Contig38743', 'Contig38753', 'Contig38760', 'Contig38784', 'Contig38786', 'Contig38840', 'Contig38841', 'Contig38900', 'Contig39014', 'Contig39073', 'Contig39075', 'Contig39088', 'Contig39091', 'Contig39093', 'Contig39124', 'Contig39190', 'Contig39242', 'Contig39246', 'Contig39312', 'Contig39375', 'Contig39380', 'Contig39423', 'Contig39431', 'Contig39442', 'Contig39531', 'Contig39583', 'Contig40233', 'Contig42531', 'Contig42701', 'Contig43931', 'Contig43976', 'Contig46767', 'Contig51182', 'Contig51300', 'Contig51893', 'Contig52158', 'Contig52744', 'Contig53672', 'Contig54161', 'Contig54345', 'Contig54416', 'Contig54657', 'Contig54919', 'Contig56049', 'Contig56304', 'Contig56802', 'Contig57969', 'Contig57989', 'Contig60862', 'Contig61052', 'Contig61060', 'Contig61109', 'Contig61172', 'Contig61187', 'Contig61244', 'Contig61342', 'Contig61501', 'Contig61565', 'Contig61754', 'Contig61768', 'Contig619', 'Contig62329', 'Contig625', 'Contig62885', 'Contig6409', 'Contig6410', 'Contig64979', 'Contig65479', 'Contig65625', 'Contig658', 'Contig66471', 'Contig66893', 'Contig66908', 'Contig67018', 'Contig67100', 'Contig67160', 'Contig67467', 'Contig67532', 'Contig8083', 'Contig814', 'Contig891', 'Contig921', 'Contig981', 'Contig982']

print('removing adapters')
genome = OrderedDict()
for contig in contigs:
	if contig.description in remove:
		pass
	else:
		for key, value in adapters.items():
			if contig.description == key:
				if len(value) == 1:
					for i in value:
						if i[0] == 1:
							genome[key] = contig.seq[i[1]:]
						elif i[1] == len(contig.seq):
							genome[key] = contig.seq[:i[0]-1]
						else:
							print(key)
				else:
					if value[0][0] == 1 and value[1][1] == len(contig.seq):
						genome[key] = contig.seq[value[0][1]:value[1][0]-1]
					else:
						print(key)
			else:
				genome[contig.description] = contig.seq

print('writing contigs to file')
for key, value in genome.items():
	print(key)
	contigs_upd.write('>{}\n{}\n'.format(key, value))

contigs_upd.close()