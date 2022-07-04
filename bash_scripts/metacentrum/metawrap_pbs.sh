#!/bin/bash
#PBS -N metawrap
#PBS -l select=1:ncpus=20:mem=150gb:scratch_local=1gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add metawrap-1.3
# module add fastQC-0.11.5
# module add trim_galore-0.6.2

data_dir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/P2S_1-01A_L001-ds.9f42a90caf694c0ab5686f0e22e79319/'

#copy files to scratch
cp $data_dir'1-reads/P2S_trimmed_1.fq.gz' $SCRATCHDIR
cp $data_dir'1-reads/P2S_trimmed_2.fq.gz' $SCRATCHDIR
cp $data_dir'2-spades/scaffolds.fasta' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

# #read trimming and QC
# mkdir read_qc
# fwd='P2S_S1_L001_R1_001.fastq.gz'
# rev='P2S_S1_L001_R2_001.fastq.gz'
# metawrap read_qc --skip-bmtagger  -t $PBS_NUM_PPN -1 $fwd -2 $rev -o read_qc

# #metagenome assembly
# metaWRAP assembly -t $PBS_NUM_PPN -m 150 --metaspades -1 reads_1.fastq -2 reads_2.fastq -o assembly

#kraken on reads and assembly
assembly='scaffolds.fasta'
metawrap kraken -o kraken -t $PBS_NUM_PPN *fq.gz $assembly

#copy files back
rm *fq.gz $assembly
cp -r * $data_dir'metawrap'
