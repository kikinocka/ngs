#!/bin/bash
#PBS -N mmseqs2
#PBS -l select=1:ncpus=15:mem=20gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

mmseqs='/storage/brno3-cerit/home/kika/miniconda3/bin/mmseqs'
data_dir='/storage/brno3-cerit/home/kika/sl_euglenozoa/v9/V9_DeepSea/decontaminated/stramenopiles/'

#copy files to scratch
cp $data_dir'eukprot_v2_proteins_renamed.taxids.faa' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

fasta='eukprot_v2_proteins_renamed.taxids.faa'

$mmseqs easy-linclust $fasta tmp --min-seq-id 0.95 -c 0.3 --cov-mode 1 --cluster-mode 2


#copy files back
rm -r $fasta tmp
cp -r * $data_dir
