#!/usr/bin/env python3
import os

os.chdir('/home/kika/ownCloud/euglenophytes/pt_proteome/')
table = open('all_spp_comparison.tsv').readlines()[1:]

def find_seqs(line):
	line = line.strip()
	eg = line.split('\t')[0]
	el = line.split('\t')[2]
	eut = line.split('\t')[4]
	rhab = line.split('\t')[6]
	spp = (eg, eut, el, rhab)
	return spp

with open('og_all.txt', 'w') as all_sp, open('og_plastid.txt', 'w') as plastid, \
	open('og_photosynthetic.txt', 'w') as photo, open('og_EGspecific.txt', 'w') as eg_spec, \
	open('og_euglena.txt', 'w') as euglena, open('og_noEut.txt', 'w') as noEut, \
	open('og_noEL.txt', 'w') as noEL, open('og_EG-Rhab.txt', 'w') as eg_rhab:
	remove_dupl = set()
	for line in table:
		spp = find_seqs(line)
		remove_dupl.add(spp)
	print(len(remove_dupl))

	for spp in remove_dupl:
		if '-' not in spp:
			spp = set(spp)
			spp = str(spp).replace('\'', '').replace('{', '').replace('}', '')
			all_sp.write('{}\n'.format(spp))

		if '-' not in spp[:3] and spp[3] == '-':
			spp = set(spp[:3])
			spp = str(spp).replace('\'', '').replace('{', '').replace('}', '')
			plastid.write('{}\n'.format(spp))

		if '-' not in spp[:2] and spp[2] == '-' and spp[3] == '-':
			spp = set(spp)
			spp.remove('-')
			spp = str(spp).replace('\'', '').replace('{', '').replace('}', '')
			photo.write('{}\n'.format(spp))

		if '-' != spp[0] and spp[1] == '-' and spp[2] == '-' and spp[3] == '-':
			spp = set(spp)
			spp.remove('-')
			spp = str(spp).replace('\'', '').replace('{', '').replace('}', '')
			eg_spec.write('{}\n'.format(spp))

		if '-' != spp[0] and spp[1] == '-' and spp[2] != '-' and spp[3] == '-':
			spp = set(spp)
			spp.remove('-')
			spp = str(spp).replace('\'', '').replace('{', '').replace('}', '')
			euglena.write('{}\n'.format(spp))

		if '-' != spp[0] and spp[1] == '-' and spp[2] != '-' and spp[3] != '-':
			spp = set(spp)
			spp.remove('-')
			spp = str(spp).replace('\'', '').replace('{', '').replace('}', '')
			noEut.write('{}\n'.format(spp))

		if '-' != spp[0] and spp[1] != '-' and spp[2] == '-' and spp[3] != '-':
			spp = set(spp)
			spp.remove('-')
			spp = str(spp).replace('\'', '').replace('{', '').replace('}', '')
			noEL.write('{}\n'.format(spp))

		if '-' != spp[0] and spp[1] == '-' and spp[2] == '-' and spp[3] != '-':
			spp = set(spp)
			spp.remove('-')
			spp = str(spp).replace('\'', '').replace('{', '').replace('}', '')
			eg_rhab.write('{}\n'.format(spp))
