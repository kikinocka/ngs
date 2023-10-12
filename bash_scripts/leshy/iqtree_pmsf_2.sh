#!/bin/bash

HOMEDIR='/mnt/mokosz/home/kika/metamonads_ancestral/OGs+HMMhits_trimal_gt-0.8'
ALNDIR='/mnt/mokosz/home/kika/metamonads_ancestral/OGs+HMMhits_iqtree'

while read -r sample
do
	iqtree2 -m LG+G4 -T AUTO --threads-max 10 --quiet --safe -s $HOMEDIR/$sample --prefix $ALNDIR/guide_${sample%.aln}
	iqtree2 -m LG+C20+G4 -T 10 -B 1000 --nmax 5000 --quiet --safe -s $HOMEDIR/$sample --tree-freq $ALNDIR/guide_${sample%.aln}.treefile --prefix $ALNDIR/${sample%.aln}
done < $HOMEDIR'/gt-0.8_to_iqt.txt' #last item must end with a newline!


python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py IQTREE2 PMSF trimal -gt 0.8 done
