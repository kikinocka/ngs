#!/bin/bash
#PBS -N metaeuk
#PBS -l select=1:ncpus=20:mem=500gb:scratch_local=1gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

data_dir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/P2S_1-01A_L001-ds.9f42a90caf694c0ab5686f0e22e79319/'
metaeuk='/storage/brno3-cerit/home/kika/miniconda3/bin/metaeuk'
database='/storage/brno3-cerit/home/kika/databases/MMETSP_uniclust50_MERC/MMETSP_uniclust50_MERC'

#copy files to scratch
cp $data_dir'5-tiara/eukarya.fasta' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

contigs='eukarya.fasta'
out='euk_metaeuk'

$metaeuk easy-predict --threads $PBS_NUM_PPN $contigs $database $out $SCRATCHDIR

#copy files back
rm $contigs
cp -r * $data_dir'6-metaeuk/database/'
