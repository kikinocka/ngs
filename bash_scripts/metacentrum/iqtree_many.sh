#!/bin/bash
#PBS -N IQT-many
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module load iqtree

data_dir='/storage/brno3-cerit/home/kika/sumk'

#copy files to scratch
cp $data_dir'/'*.aln $SCRATCHDIR

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

	iqtree -m LG+F+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s ${f} -pre $guide
	iqtree -m LG+C20+F+G -nt AUTO -ntmax $PBS_NUM_PPN -B $bb -quiet -s ${f} -ft $guide_tree #-wsr
done

#copy files back
rm *.aln
cp * $data_dir
