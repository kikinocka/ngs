#!/bin/bash
#PBS -N vsearch
#PBS -l select=1:ncpus=1:mem=1gb:scratch_local=5gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add vsearch-1.4.4

data_dir='/storage/brno3-cerit/home/kika/tRNAs-kinetoplastids/'

#copy files to scratch
cp $data_dir'Tbruc427_DNA.bw2_mapped.fq.gz' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

mapped='Tbruc427_DNA.bw2_mapped.fq.gz'
output='Tbruc428_DNA.bw2_mapped_vsearch.fa'

vsearch --derep_fulllength $mapped --output $output --sizeout


#copy files back
rm $mapped
cp * $data_dir
