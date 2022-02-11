#!/bin/bash
#PBS -N vsearch
#PBS -l select=1:ncpus=1:mem=1gb:scratch_local=5gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add vsearch/vsearch-2.14.1-intel-19.0.4-sglyhgb

data_dir='/storage/brno3-cerit/home/kika/tRNAs-kinetoplastids/'

#copy files to scratch
cp $data_dir'bw2/KP/Tbruc427_DNA.bw2_mapped.fq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

mapped='Tbruc427_DNA.bw2_mapped.fq.gz'
output='Tbruc427_DNA.bw2_mapped_vsearch.KP.fa'

vsearch --derep_fulllength $mapped --output $output --sizeout


#copy files back
rm $mapped
cp * $data_dir
