#!/bin/bash
#PBS -N IQT-many
#PBS -l select=1:ncpus=15:mem=20gb:scratch_local=10gb
#PBS -l walltime=96:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load iqtree

data_dir='/storage/brno12-cerit/home/kika/kinetoplastids/GP63'

#copy files to scratch
cp $data_dir'/'*trimal_at1.aln $SCRATCHDIR

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

	iqtree -m LG+G4 -T AUTO --threads-max $PBS_NUM_PPN --quiet --safe -s ${f} --prefix $guide
	iqtree -m LG+C20+G4 -T $PBS_NUM_PPN -B $bb --nmax $nm --quiet --safe -s ${f} --boot-trees --tree-freq $guide_tree
done

#copy files back
rm *.aln
cp * $data_dir
