#!/bin/bash

HOMEDIR='/mnt/mokosz/home/kika/metamonads_ancestral/OGs+HMMhits_trimal_gt-0.8'
ALNDIR='/mnt/mokosz/home/kika/metamonads_ancestral/OGs+HMMhits_iqtree'

while read -r sample
do
	echo $sample
	# iqtree -m LG+G -nt AUTO -ntmax 10 -quiet -safe -s $HOMEDIR/$sample -pre $ALNDIR/guide_${sample%.aln}
	# iqtree -m LG+C20+G -nt AUTO -ntmax 10 -bb 1000 -nm 5000 -quiet -safe -s $HOMEDIR/$sample -ft $ALNDIR/guide_${sample%.aln}.treefile -pre $ALNDIR/${sample%.aln}
	
	iqtree -m LG+C20+G -nt AUTO -ntmax 10 -bb 1000 -nm 5000 -quiet -safe -s $HOMEDIR/$sample -pre $ALNDIR/${sample%.aln}

	# iqtree2 -m LG+G4 -T AUTO --threads-max 10 --quiet --safe -s $HOMEDIR/$sample --prefix $ALNDIR/guide_${sample%.aln}
	# iqtree2 -m LG+C20+G4 -T 10 -B 1000 --nmax 5000 --quiet --safe -s $HOMEDIR/$sample --tree-freq $ALNDIR/guide_${sample%.aln}.treefile --prefix $ALNDIR/${sample%.aln}
done < $HOMEDIR'/gt-0.8_to_iqt.txt' #last item must end with a newline!


python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py IQTREE PMSF trimal -gt 0.8 done
