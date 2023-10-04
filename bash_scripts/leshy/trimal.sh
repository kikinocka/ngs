#!/bin/bash

#align denovo
# cd '/mnt/mokosz/home/kika/metamonads_ancestral/OGs+HMMhits_muscle/'

# for f in *.muscle.aln ; do
# 	echo $f
	
# 	# out=${f%.muscle.aln}.trimal_at1.aln
# 	# trimal -in $f -out $out -automated1 -fasta
	
# 	# out=${f%.muscle.aln}.trimal_gt-0.8.aln
# 	# trimal -in $f -out $out -gt 0.8 -fasta

# 	out=${f%.muscle.aln}.trimal_gt-0.5_cons-50.aln
# 	trimal -in $f -out $out -gt 0.5 -cons 50 -fasta
# done

HOMEDIR='/mnt/mokosz/home/kika/metamonads_ancestral/OGs+HMMhits_muscle'
ALNDIR='/mnt/mokosz/home/kika/metamonads_ancestral/OGs+HMMhits_trimal_gt-0.5_cons-50'

while read -r sample
do
	if [ ! -e $ALNDIR/${sample/muscle.aln/trimal_gt-0.5_cons-50.aln} ]; then
		touch $ALNDIR/${sample/muscle.aln/trimal_gt-0.5_cons-50.aln}
		trimal -in $HOMEDIR/$sample -out $ALNDIR/${sample/muscle.aln/trimal_gt-0.5_cons-50.aln} -gt 0.5 -cons 50 -fasta
    fi
done < $HOMEDIR'/large.txt' #last item must end with a newline!

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py trimAl done
