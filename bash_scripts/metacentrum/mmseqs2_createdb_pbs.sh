#!/bin/bash
#PBS -N mmseqs2
#PBS -l select=1:ncpus=10:mem=20gb:scratch_local=30gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

mmseqs='/storage/brno3-cerit/home/kika/miniconda3/bin/mmseqs'
data_dir='/storage/brno3-cerit/home/kika/databases/eukprot/'

#copy files to scratch
cp $data_dir'eukprot_v2_proteins_renamed.taxids.faa' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

database='eukprot_v2_proteins_renamed.taxids.faa'
out='eukprot'

$mmseqs createdb $database $out

#copy files back
rm $database
cp -r * $data_dir
