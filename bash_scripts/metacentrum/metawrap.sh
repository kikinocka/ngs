#!/bin/bash
#PBS -N metawrap
#PBS -l select=1:ncpus=20:mem=70gb:scratch_local=50gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

data_dir='/storage/brno3-cerit/home/kika/ciliates/condylostoma/'

#copy files to scratch
cp $data_dir'GCA_001499635.1_Condy_MAC_genomic.fna' $SCRATCHDIR
cp $data_dir'reads/all_reads_trimmed.fq' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

module add conda-modules-py37
conda activate metawrap-env

assembly='GCA_001499635.1_Condy_MAC_genomic.fna'

#initial binning
metawrap binning -t $PBS_NUM_PPN -m 50 --metabat2 --maxbin2 --concoct -a $assembly -o initial_binning *fq
#reads have to be unzipped

#bin refinment
metawrap bin_refinement -t $PBS_NUM_PPN -m 50 \
	-c 70 -x 10 \
	-o bin_refinement -A initial_binning/metabat2_bins -B initial_binning/maxbin2_bins -C initial_binning/concoct_bins
# -c INT	minimum % completion of bins [should be >50%] (default=70)
# -x INT	maximum % contamination of bins that is acceptable (default=10)
# -A STR	folder with metagenomic bins (files must have .fa or .fasta extension)
# -B STR	another folder with metagenomic bins
# -C STR	another folder with metagenomic bins

#visualization, 70 GB memory, 8 CPUs
metawrap blobology -t $PBS_NUM_PPN --bins bin_refinement/metawrap_bins -a $assembly -o blobology *fq


#copy files back
rm *fq $assembly
cp -r * $data_dir'metawrap'
