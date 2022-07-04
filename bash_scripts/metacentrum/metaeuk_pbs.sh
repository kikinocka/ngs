#!/bin/bash
#PBS -N metaeuk
#PBS -l select=1:ncpus=20:mem=500gb:scratch_local=1gb
#PBS -l walltime=48:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

data_dir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/P3S_1-02B_L001-ds.971c07c67a83443891de04bf749cee0b/'
metaeuk='/storage/brno3-cerit/home/kika/miniconda3/bin/metaeuk'
database='/storage/brno3-cerit/home/kika/databases/MMETSP_uniclust50_MERC/MMETSP_uniclust50_MERC_profiles'
# database='/storage/brno3-cerit/home/kika/databases/MMETSP_uniclust50_MERC/MMETSP_uniclust50_MERC'

#copy files to scratch
cp $data_dir'4-tiara/eukarya_P3S_scaffolds.fasta' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

contigs='eukarya_P3S_scaffolds.fasta'
out='euk_P3S_metaeuk'

$metaeuk easy-predict $contigs $database $out $SCRATCHDIR

#copy files back
rm $contigs
cp -r * $data_dir'5-metaeuk/'
