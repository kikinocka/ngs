#!/bin/bash
#PBS -N IQT-many
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=10gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module load iqtree

data_dir='/storage/brno12-cerit/home/kika/membrane-trafficking/dicty_JPP/RABs/spp/more/'

#copy files to scratch
cp $data_dir'Atha.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'Bsal.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'Ddis.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'Egra.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'Hsap.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'Nfow.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'Ppap.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'Scer.trimal_gt-0.8.aln' $SCRATCHDIR
cp $data_dir'Tbru.trimal_gt-0.8.aln' $SCRATCHDIR


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
	iqtree3-mpi -m LG+C20+G -T $PBS_NUM_PPN -B $bb --alrt $bb --nmax $nm --quiet --safe -s $aln --tree-freq $guide_tree --boot-trees
done

#copy files back
rm *.aln
cp * $data_dir && clean_scratch
