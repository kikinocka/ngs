#!/bin/bash
#PBS -N metaeuk
#PBS -l select=1:ncpus=20:mem=100gb:scratch_local=350gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

data_dir='/storage/brno12-cerit/home/kika/cz-au_fire/'
metaeuk='/storage/brno3-cerit/home/kika/miniconda3/bin/metaeuk'
db_dir='/storage/brno3-cerit/home/kika/databases/MMETSP_uniclust50_MERC/'

#copy files to scratch
cp $data_dir'whokaryote_out/eukaryotes.fasta' $SCRATCHDIR
cp $db_dir'MMETSP_uniclust50_MERC' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

database='MMETSP_uniclust50_MERC'
contigs='eukaryotes.fasta'
out='eukarya_metaeuk'

$metaeuk easy-predict $contigs $database $out $SCRATCHDIR --threads $PBS_NUM_PPN

#copy files back
rm $contigs $database
cp -r * $data_dir'metaeuk/'
