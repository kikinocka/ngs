#!/bin/bash
#PBS -N IQT-many4
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=168:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-1.6.12

data_dir='/storage/brno3-cerit/home/kika/metamonads/'

#copy files to scratch
# cp $data_dir'/'*.aln $SCRATCHDIR
cp 'q2012690.og_hmm.trimal_gt-0.8.filtered-50.aln' $SCRATCHDIR
cp 'q2012965.og_hmm.trimal_gt-0.8.filtered-50.aln' $SCRATCHDIR
cp 'q2019593.og_hmm.trimal_gt-0.8.filtered-50.aln' $SCRATCHDIR
cp 'q2012707.og_hmm.trimal_gt-0.8.filtered-50.aln' $SCRATCHDIR
cp 'q2012987.og_hmm.trimal_gt-0.8.filtered-50.aln' $SCRATCHDIR
cp 'q2019788.og_hmm.trimal_gt-0.8.filtered-50.aln' $SCRATCHDIR
cp 'q2012723.og_hmm.trimal_gt-0.8.filtered-50.aln' $SCRATCHDIR
cp 'q2014726.og_hmm.trimal_gt-0.8.filtered-50.aln' $SCRATCHDIR
cp 'q2019794.og_hmm.trimal_gt-0.8.filtered-50.aln' $SCRATCHDIR
cp 'q2012725.og_hmm.trimal_gt-0.8.filtered-50.aln' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for f in *.aln ; do
	echo ${f}
	guide=guide_${f%.aln}
	guide_tree=$guide'.treefile'
	bb=1000
	nm=5000
	
	# iqtree -m TEST -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -nm $nm -quiet -s ${f}
	# iqtree -m GTR+G -nt AUTO -ntmax $PBS_NUM_PPN -b $bb -quiet -s ${f}

	# iqtree -m LG+F+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s ${f} -pre $guide
	# iqtree -m LG+C20+F+G -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -quiet -s ${f} -ft $guide_tree #-wsr


	iqtree -m LG+C20+G -nt AUTO -ntmax $PBS_NUM_PPN -bb 1000 -nm 5000 -quiet -safe -s ${f} -pre ${f%.aln}

done

#copy files back
rm *.aln
cp * $data_dir
