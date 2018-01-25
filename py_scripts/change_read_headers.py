#!/usr/bin/python3
import os

os.chdir('/media/4TB1/blastocrithidia/kika_workdir/reads/')
files = os.listdir()

for file in files:
	if '.fq' in file:
		print(file)
		SRR = file.split('_')[0]
		pair = file.split('_')[2].split('.')[0]
		infile = open(file).read()
		lines = infile.split('\n')
		for line in lines:
			out = open(SRR + '_trimmed_renamed_' + pair + '.fq', 'a')
			if line.startswith('@HWI'):
				# @HWI-ST942:114:C11YJACXX:3:1101:3080:2460_forward/1
				# @HWI-ST942:114:C11YJACXX:3:1101:3080:2460_reverse/2
				print(line)
				description = line.split('_')[0] + '/' + line.split('_')[1].split('/')[1]
				out.write(description + '\n')
			elif line.startswith('@GWZ'):
				# @GWZHISEQ01:84:D0V9TACXX:2:1101:7691:1834_forward/1
				# @GWZHISEQ01:84:D0V9TACXX:2:1101:7691:1834_reverse/2
				print(line)
				description = line.split('_')[0] + '/' + line.split('_')[1].split('/')[1]
				out.write(description + '\n')
			else:
				out.write(line + '\n')
			out.close()