#!/bin/bash
#PBS -N metabat
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module load metabat


data_dir='/storage/brno3-cerit/home/kika/ciliates/condylostoma/'

#copy data to scratch
cp $data_dir'GCA_001499635.1_Condy_MAC_genomic.fna' $SCRATCHDIR
cp $data_dir'all_reads_trimmed.fq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

#copy files back
rm 
cp -r * $data_dir
