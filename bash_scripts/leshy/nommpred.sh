#!/bin/sh

cd '/mnt/mokosz/home/kika/workdir/'

mit=1
mro=2
dict=5
tryp=9
toxo=8
stram=7
# 1) Mt
# 2) MRO
# 3) Piroplasma
# 4) Chlorophyta
# 5) Dictyostelium
# 6) Plasmodium
# 7) stramenopiles
# 8) Toxoplasma
# 9) Trypanosomatida

for file in *.fa; do
	echo $file

	# out=${file%.*}'.nommpred_mro.txt'
	# NommPred.py -i $file -o $out -l $mro --overwrite

	# out=${file%.*}'.nommpred_dict.txt'
	# NommPred.py -i $file -o $out -l $dict --overwrite

	out=${file%.*}'.nommpred_mt.txt'
	NommPred.py -i $file -o $out -l $mit --overwrite

	# out=${file%.*}'.nommpred_tryp.txt'
	# NommPred.py -i $file -o $out -l $tryp --overwrite

	# out=${file%.*}'.nommpred_toxo.txt'
	# NommPred.py -i $file -o $out -l $toxo --overwrite

	# out=${file%.*}'.nommpred_stram.txt'
	# NommPred.py -i $file -o $out -l $stram --overwrite
done

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py NommPred done
