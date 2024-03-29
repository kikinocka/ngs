#!/bin/bash
#PBS -N TransDecoder_longORFs
#PBS -l select=1:ncpus=1:mem=2gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
source /cvmfs/software.metacentrum.cz/modulefiles/5.1.0/loadmodules
module load transdecoder

data_dir='/storage/brno3-cerit/home/kika/UGA_decoding/nyctotherus/trinity/'

#copy files to scratch
cp $data_dir'Trinity.fasta' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

transcriptome='Trinity.fasta'
TransDecoder.LongOrfs -t $transcriptome #--genetic_code Euplotid

#copy files back
rm $transcriptome
cp -r * $data_dir
