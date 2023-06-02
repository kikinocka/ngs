#!/bin/bash
#PBS -N metabat
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=10gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module load metabat/2.15-gcc-10.2.1-2nf5o7t


data_dir='/storage/brno3-cerit/home/kika/ciliates/condylostoma/'

#copy data to scratch
cp $data_dir'GCA_001499635.1_Condy_MAC_genomic.fna' $SCRATCHDIR
cp $data_dir'mapping/condy_sorted.bam' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR
genome='GCA_001499635.1_Condy_MAC_genomic.fna'
bamfile='condy_sorted.bam'
depth='condy_depth.txt'
min_contig=1500
min_samples=3

jgi_summarize_bam_contig_depths --outputDepth $depth $bamfile
metabat1 -t $PBS_NUM_PPN -m $min_contig -i --minSamples $min_samples $genome -a $depth -o $SCRATCHDIR

#copy files back
rm $genome $bamfile
cp -r * $data_dir'metabat'
