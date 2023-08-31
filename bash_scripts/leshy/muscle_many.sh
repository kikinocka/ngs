#!/bin/bash
#name prefetch_wrapper

HOMEDIR='/mnt/mokosz/home/kika/metamonads_ancestral/OGs+HMMhits_fasta'
ALNDIR='/mnt/mokosz/home/kika/metamonads_ancestral/OGs+HMMhits_muscle'

#cd $HOMEDIR

while read -r sample
do
	if [ ! -e $ALNDIR/${sample/fa/muscle.aln} ]; then
		touch $ALNDIR/${sample/fa/muscle.aln}
	    muscle5.1 -super5 $HOMEDIR/$sample -output $ALNDIR/${sample/fa/muscle.aln} -threads 15
    fi
done < 'large.txt' #last item must end with a newline!

python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py muscle5 done

