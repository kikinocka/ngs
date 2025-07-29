#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N IQT2
#PBS -l nodes=1:ppn=15
#PBS -l walltime=900:00:00


cd '/home/users/kika/workdir/'

# aln='gp63.trimal_at1.aln'
# guide='guide_gp63.trimal_at1'
# guide_tree=$guide'.treefile'
bb=1000
nm=5000


# iqtree -m LG+G4 -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s $aln --prefix $guide
# iqtree -m LG+C60+G4 -T $PBS_NUM_PPN -B $bb --nmax $nm --quiet --safe -s $aln --boot-trees --tree-freq $guide_tree
iqtree2 -s combinedArfsRoot__Carpedi_Arf6_removed.phy -nt AUTO -m LG+C60+R10 -keep_empty_seq -te combinedArfs_Carpedi_Arf6_removed_rooted.treefile -asr


python /home/users/kika/scripts/py_scripts/slackbot.py OSU: IQT2 done
