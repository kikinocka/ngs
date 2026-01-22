#!/bin/bash
#PBS -N IQT-many
#PBS -l select=1:ncpus=15:mem=20gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load iqtree

data_dir='/storage/brno12-cerit/home/kika/kinetoplastids/RNAi/ver2'

#copy files to scratch
cp $data_dir'/'* $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

for aln in *.aln ; do
	echo ${aln}
	guide=guide_${aln%.aln}
	guide_tree=$guide'.treefile'
	bb=1000
	nm=5000
	
	# iqtree -m TEST -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -nm $nm -quiet -s ${aln}
	# iqtree -m GTR+G -nt AUTO -ntmax $PBS_NUM_PPN -b $bb -quiet -s ${aln}

	iqtree3-mpi -m LG+G -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s $aln --prefix $guide
	iqtree3-mpi -m LG+C60+G -T $PBS_NUM_PPN -B $bb --alrt $nm --nmax $nm --quiet --safe -s $aln --tree-freq $guide_tree --boot-trees
done

#copy files back
rm *.aln
cp * $data_dir
