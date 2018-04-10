#!/usr/bin/python3

blast_out = open('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/chlamydia_search/eg_yosh/EG_Yoshida_GDJR01.1.tax')
first_annot = open('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/chlamydia_search/eg_yosh/eg_yosh_names.tsv')

find = {}
for line in first_annot:
	find[line.split('\t')[0]] = [line.split('\t')[1][:-1]]

for line in blast_out:
	if line.split('\t')[0] in find:
		if ('hypothetical' not in line.split('\t')[6] and 'predicted' not in line.split('\t')[6] and 
		'unknown' not in line.split('\t')[6] and 'Hypothetical' not in line.split('\t')[6]):
			find[line.split('\t')[0]].append(line.split('\t')[6][:-1])

with open('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/chlamydia_search/eg_yosh/eg_yosh_annotations.tsv', 'w') as out:
	for key, value in find.items():
		if 'hypothetical' in value[0]:
			if len(value) == 1:
				out.write('{}\t{}\n'.format(key, value[0]))
			else:
				out.write('{}\t{}\t{}\n'.format(key, value[0], value[1]))
		else:
			out.write('{}\t{}\n'.format(key, value[0]))
