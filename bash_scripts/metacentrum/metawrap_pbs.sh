#!/bin/bash
#PBS -N metawrap
#PBS -l select=1:ncpus=20:mem=5gb:scratch_local=1gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add metawrap-1.3

data_dir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/P2S_1-01A_L001-ds.9f42a90caf694c0ab5686f0e22e79319/'

#copy files to scratch
cp $data_dir'1-reads/P2S_S1_L001_R1_001.fastq.gz' $SCRATCHDIR
cp $data_dir'1-reads/P2S_S1_L001_R2_001.fastq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

mkdir read_qc
fwd='P2S_S1_L001_R1_001.fastq.gz'
rev='P2S_S1_L001_R2_001.fastq.gz'
metawrap read_qc --skip-bmtagger  -t $PBS_NUM_PPN -1 $fwd -2 $rev -o read_qc


#copy files back
rm $fwd $rev
cp -r * $data_dir'metawrap'
