#!/bin/bash
#PBS -N metabat
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=10gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module load metabat


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

jgi_summarize_bam_contig_depths --outputDepth $depth $bamfile
metabat -t $PBS_NUM_PPN -m $min_contig -i $genome -a $depth -o $SCRATCHDIR

#copy files back
rm $genome $bamfile
cp -r * $data_dir'metabat'
