#!/bin/bash
#PBS -N metawrap
#PBS -l select=1:ncpus=20:mem=150gb:scratch_local=1gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add metawrap-1.3

data_dir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/P2S_1-01A_L001-ds.9f42a90caf694c0ab5686f0e22e79319/'

#copy files to scratch
cp $data_dir'1-reads/P2S_trimmed_1.fq.gz' $SCRATCHDIR
cp $data_dir'1-reads/P2S_trimmed_2.fq.gz' $SCRATCHDIR
cp $data_dir'2-spades/scaffolds.fasta' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

assembly='scaffolds.fasta'
metawrap binning -t $PBS_NUM_PPN -m 150 --metabat2 --maxbin2 --concoct -a $assembly -o initial_binning *fq.gz

#copy files back
rm *fq.gz $assembly
cp -r * $data_dir'metawrap'
