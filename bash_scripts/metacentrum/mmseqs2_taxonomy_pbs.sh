#!/bin/bash
#PBS -N mmseqs2
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=30gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

mmseqs='/storage/brno3-cerit/home/kika/miniconda3/bin/mmseqs'
db_dir='/storage/brno3-cerit/home/kika/databases/eukprotDB/'
data_dir='/auto/brno3-cerit/nfs4/home/kika/oil_sands/metagenomes/20200821_BML-P3B/8-metaeuk/profiles/'

#copy files to scratch
cp $db_dir'eukprotDB' $SCRATCHDIR
cp $data_dir'euk_metaeuk.fas' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

database='eukprotDB'
query='euk_metaeuk.fas'
taxonomy='euk_metaeuk.taxonomy'

$mmseqs taxonomy $query $database $taxonomy tmp --tax-output-mode 2 --threads $PBS_NUM_PPN
#--tax-output-mode INT   0: output LCA, 1: output alignment 2: output both [0]

#copy files back
rm -r $database $query tmp
cp -r * $data_dir'9-mmseqs2'
