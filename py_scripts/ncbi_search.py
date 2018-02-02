#!/usr/bin/python3
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "zahonova.kristina@gmail.com"

ids = [
	'KU356490.1', 'KU356491.1', 'KU356492.1', 'KU356493.1', 'KU356494.1', 'KU356495.1', 'KU356496.1', 'KU356497.1', 
	'KU356500.1', 'KU356501.1', 'KU356503.1', 'KU356504.1', 'KU356505.1', 'KU356506.1', 'KU356507.1', 'HQ288823.1', 
	'EU123536.1', 'KU356508.1', 'KU356510.1', 'KU356511.1', 'KU356512.1', 'KU356513.1', 'KU356514.1', 'KU356515.1', 
	'KU356516.1', 'KU356517.1', 'KU356518.1', 'KU356519.1', 'KU356520.1', 'KU356522.1', 'KU356523.1', 'KU356525.1', 
	'KU356527.1', 'KU356537.1', 'KU356538.1', 'KU356529.1', 'KU356530.1', 'KU356531.1', 'KU356532.1', 'KU356533.1', 
	'KU356534.1', 'KU356535.1', 'KU356536.1', 'KU356539.1', 'KU356540.1', 'KU356541.1', 'KU356543.1', 'KU356544.1', 
	'HQ288824.1', 'KU356546.1', 'JQ302962.1', 'KU356547.1', 'KU356548.1', 'KU356550.1', 'KU356554.1', 'KU356555.1', 
	'KU356557.1', 'KU356558.1', 'KU356562.1', 'KU356563.1', 'KU356564.1', 'KU356565.1', 'KU356568.1', 'KU356569.1', 
	'KU356570.1', 'KU356498.1', 'KU356499.1', 'KU356502.1', 'EU123537.1', 'KU356509.1', 'KU356521.1', 'KU356524.1', 
	'KU356526.1', 'KU356528.1', 'KU356542.1', 'KU356545.1', 'KU356549.1', 'KU356551.1', 'KU356552.1', 'KU356553.1', 
	'KU356556.1', 'KU356559.1', 'KU356560.1', 'KU356561.1', 'KU356566.1', 'KU356567.1']

with open('/home/kika/MEGAsync/diplonema_mt/Dp_mt_genome/dp_mt.txt', 'w') as out:
	for nucl_id in ids:
		nucl = Entrez.efetch(db='nucleotide', id=nucl_id, rettype='gb', retmode='text')
		nucl_record = SeqIO.read(nucl, 'genbank')
		print(nucl_record.description[:-1])
		out.write('>{}\n{}\n'.format(nucl_record.description[:-1], nucl_record.seq))