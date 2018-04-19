import os

names = open('specrenamelist.tsv', 'r')
name_dict = {}
badchars = (",:;()'")

for name in names:
	splitline = name.split('\t')
	specname = splitline[1]
	specname = ''.join(c for c in specname if c not in badchars)
	print(specname)
	name_dict[splitline[0]] = specname

files = os.listdir('.')
files = [f for f in files if f.endswith(".treefile")]

for f in files:
	with open(f) as strom, open(f.split(".treefile")[0] + "_renamed.treefile", "w") as result:
		strom_line = strom.readline()
		for key in name_dict:
			strom_line = strom_line.replace(key, name_dict[key])
		result.write(strom_line)
	
