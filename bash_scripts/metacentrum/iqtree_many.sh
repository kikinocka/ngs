#!/bin/bash
#PBS -N IQT-many
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
# module add iqtree-1.6.12
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module load iqtree

data_dir='/storage/brno12-cerit/home/kika/kinetoplastids/RNAi/'

#copy files to scratch
cp $data_dir'/'*.aln $SCRATCHDIR
# cp $data_dir'q2007348.og_hmm.trimal_gt-0.8.filtered-50.aln' $SCRATCHDIR
# cp $data_dir'q2009078.og_hmm.trimal_gt-0.8.filtered-50.aln' $SCRATCHDIR
# cp $data_dir'q2009173.og_hmm.trimal_gt-0.8.filtered-50.aln' $SCRATCHDIR
# cp $data_dir'q2011721.og_hmm.trimal_gt-0.8.filtered-50.aln' $SCRATCHDIR
# cp $data_dir'q2011742.og_hmm.trimal_gt-0.8.filtered-50.aln' $SCRATCHDIR
# cp $data_dir'q2012707.og_hmm.trimal_gt-0.8.filtered-50.aln' $SCRATCHDIR
# cp $data_dir'q2019788.og_hmm.trimal_gt-0.8.filtered-50.aln' $SCRATCHDIR
# cp $data_dir'q2019794.og_hmm.trimal_gt-0.8.filtered-50.aln' $SCRATCHDIR


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

	# iqtree -m LG+C20+G -nt AUTO -ntmax $PBS_NUM_PPN -bb 1000 -nm 10000 -quiet -safe -s ${f} -pre ${f%.aln}

	iqtree2 -m LG+G4 -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s ${f} --prefix $guide
	iqtree2 -m LG+C20+G4 -T 15 -B $bb --nmax $nm --quiet --safe -s ${f} --tree-freq $guide_tree

done

#copy files back
rm *.aln
cp * $data_dir
