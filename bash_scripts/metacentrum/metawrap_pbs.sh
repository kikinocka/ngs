#!/bin/bash
#PBS -N metawrap
#PBS -l select=1:ncpus=20:mem=150gb:scratch_local=20gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

data_dir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/P2S_1-01A_L001-ds.9f42a90caf694c0ab5686f0e22e79319/'

#copy files to scratch
cp $data_dir'1-reads/P2S_trimmed_1.fastq' $SCRATCHDIR
cp $data_dir'1-reads/P2S_trimmed_2.fastq' $SCRATCHDIR
cp $data_dir'2-spades/scaffolds.fasta' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

assembly='scaffolds.fasta'

module add conda-modules-py37
conda activate metawrap-env
metawrap binning -t $PBS_NUM_PPN -m 150 --metabat2 --maxbin2 --concoct -a $assembly -o initial_binning *fastq
#reads have to be unzipped

#copy files back
rm *fastq $assembly
cp -r * $data_dir'metawrap'
