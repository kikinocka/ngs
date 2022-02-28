#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/archamoebae/ribosomal_proteins/local_query_files/')
files = [x for x in os.listdir() if x.endswith('.faa')]

protein_dic = {'EHI020280' : 'S2', 'EHI146340' : 'S3', 'EHI050280' : 'S3a', 'EHI057850' : 'S4', 'EHI126110' : 'S5', 
	'EHI000590' : 'S6', 'EHI067530' : 'S7', 'EHI009870' : 'S8e', 'EHI125780' : 'S9', 'EHI197030' : 'S10', 'EHI124850' : 'S11', 
	'EHI111760' : 'S12', 'EHI112880' : 'S13', 'EHI074090' : 'S14', 'EHI046690' : 'S15', 'EHI073600' : 'S15a', 'EHI008010' : 'S16', 
	'EHI009810' : 'S17', 'EHI009680' : 'S18', 'EHI146570' : 'S19', 'EHI026410' : 'S20', 'EHI126870' : 'S21', 'EHI020310' : 'S23', 
	'EHI078300' : 'S24', 'EHI074800' : 'S25', 'EHI039010' : 'S26', 'EHI152230' : 'S27', 'EHI036530' : 'S27a', 'EHI021450' : 'S28', 
	'EHI126250' : 'S29', 'EHI044550' : 'S30', 'EHI081410' : 'SA', 'EHI201830' : 'L1', 'EHI127200' : 'L2-L8', 'EHI005890' : 'L3', 
	'EHI000510' : 'L4', 'EHI006860' : 'L5', 'EHI045300' : 'L6', 'EHI010650' : 'L7', 'EHI029530' : 'L7a', 'EHI126140' : 'L9', 
	'EHI044810' : 'L10', 'EHI135790' : 'L10a', 'EHI038580' : 'L11', 'EHI030710' : 'L12', 'EHI181560' : 'L13', 'EHI200090' : 'L13A', 
	'EHI184470' : 'L14', 'EHI020300' : 'L15', 'EHI054740' : 'L17', 'EHI079190' : 'L18', 'EHI035600' : 'L18a', 'EHI096850' : 'L19', 
	'EHI069110' : 'L21', 'EHI141940' : 'L22e', 'EHI051710' : 'L23', 'EHI182850' : 'L23A', 'EHI030760' : 'L24', 'EHI111570' : 'L26', 
	'EHI146370' : 'L27', 'EHI069490' : 'L27a', 'EHI023220' : 'L29', 'EHI065740' : 'L30', 'EHI058080' : 'L31', 'EHI044770' : 'L32', 
	'EHI164870' : 'L34', 'EHI042720' : 'L35', 'EHI014110' : 'L35a', 'EHI124330' : 'L36', 'EHI015320' : 'L37', 'EHI008650' : 'L37a', 
	'EHI023840' : 'L38', 'EHI143430' : 'L39', 'EHI092470' : 'L40', 'EHI092120' : 'L44', 'EHI042920' : 'P1', 'EHI090400' : 'P0', 
	'EHI138770' : 'P2', 'EHI102940' : 'PO'}

for file in files:
	print(file)
	name = file.split('.faa')[0]
	if name in protein_dic.keys():
		new = '{}.faa'.format(protein_dic[name])
		with open(new, 'w') as out:
			for line in open(file):
				out.write(line)
