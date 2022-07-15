#!/bin/bash
#PBS -N metawrap
#PBS -l select=1:ncpus=16:mem=50gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

data_dir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/P2S_1-01A_L001-ds.9f42a90caf694c0ab5686f0e22e79319/'

#copy files to scratch
cp -r $data_dir'1-reads/'*fastq $SCRATCHDIR
cp -r $data_dir'2-spades/scaffolds.fasta' $SCRATCHDIR
cp -r $data_dir'metawrap/bin_refinement_50_10/metawrap_50_10_bins' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

assembly='scaffolds.fasta'

module add conda-modules-py37
conda activate metawrap-env

# #initial binning
# metawrap binning -t $PBS_NUM_PPN -m 50 --metabat2 --maxbin2 --concoct -a $assembly -o initial_binning *fastq
# #reads have to be unzipped

# #bin refinment
# metawrap bin_refinement -t $PBS_NUM_PPN -m 50 \
# 	-c 50 -x 10 \
# 	-o bin_refinement_50_10 -A metabat2_bins -B maxbin2_bins -C concoct_bins
# # -c INT	minimum % completion of bins [should be >50%] (default=70)
# # -x INT	maximum % contamination of bins that is acceptable (default=10)
# # -A STR	folder with metagenomic bins (files must have .fa or .fasta extension)
# # -B STR	another folder with metagenomic bins
# # -C STR	another folder with metagenomic bins

#visualization
metawrap blobology -t $PBS_NUM_PPN --bins metawrap_50_10_bins -a $assembly -o blobology_50_10 *fastq


#copy files back
rm *fastq $assembly
rm -r metawrap_50_10_bins
cp -r * $data_dir
