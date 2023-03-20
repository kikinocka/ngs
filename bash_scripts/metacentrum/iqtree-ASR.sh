#!/bin/bash
#PBS -N IQT-ASR
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-1.6.12

data_dir='/storage/brno3-cerit/home/kika/trafficking/AP1S'

#copy files to scratch
cp $data_dir'/'*.aln $SCRATCHDIR
cp $data_dir'/'*.constr1 $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

constr1='AP1S.constr1'
for f in *.aln ; do
	guide=guide_${f%.aln}
	guide_tree=$guide'.treefile'
	bb=1000
	nm=5000
	iqtree -m TEST -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -nm $nm -quiet -s ${f} -g $constr1 -asr
done

#copy files back
rm *.aln
cp * $data_dir
