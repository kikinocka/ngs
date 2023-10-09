#!/bin/bash

# cd '/mnt/mokosz/home/kika/workdir/'

# for aln in *.aln ; do
# 	echo $aln
# 	guide=guide_${aln%.aln}
# 	guide_tree=$guide'.treefile'
# 	bb=1000
# 	nm=5000
# 	# iqtree -m LG+G -nt AUTO -ntmax 10 -quiet -s ${aln} -pre $guide
# 	# iqtree -m LG+C20+G -nt AUTO -ntmax 10 -bb $bb -nm $nm -quiet -s ${aln} -ft $guide_tree

# 	iqtree2 -m LG+G4 -T AUTO --threads-max 15 --quiet --safe -s $aln --prefix $guide
# 	iqtree2 -m LG+C20+G4 -T AUTO --threads-max 15 -B $bb --nmax $nm --quiet --safe -s $aln --tree-freq $guide_tree
# done


HOMEDIR='/mnt/mokosz/home/kika/metamonads_ancestral/OGs+HMMhits_trimal_automated1'
ALNDIR='/mnt/mokosz/home/kika/metamonads_ancestral/OGs+HMMhits_iqtree'

while read -r sample
do
	bb=1000
	nm=5000
	if [ ! -e $ALNDIR/guide_${sample%.aln} ]; then
		touch $ALNDIR/guide_${sample%.aln}
		iqtree2 -m LG+G4 -T AUTO --threads-max 15 --quiet --safe -s $HOMEDIR/$sample --prefix $ALNDIR/guide_${sample%.aln}
    fi
    if [ ! -e $ALNDIR/guide_${sample%.aln}.treefile ]; then
		touch $ALNDIR/guide_${sample%.aln}.treefile
		iqtree2 -m LG+C20+G4 -T AUTO --threads-max 15 -B $bb --nmax $nm --quiet --safe -s $HOMEDIR/$sample --tree-freq $ALNDIR/guide_${sample%.aln}.treefile
done < $HOMEDIR'/at1_to_iqt.txt' #last item must end with a newline!


# python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py IQTREE PMSF done
python3 /mnt/mokosz/home/kika/scripts/py_scripts/slackbot.py IQTREE2 PMSF done
