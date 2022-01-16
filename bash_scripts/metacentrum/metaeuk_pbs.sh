#!/bin/bash
#PBS -N metaeuk
#PBS -l select=1:ncpus=20:mem=200gb:scratch_local=1gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

data_dir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/P1B_1-05C_L001-ds.ec8b691bd68b44deb59919ca3da275ba/'
metaeuk='/storage/brno3-cerit/home/kika/miniconda3/bin/metaeuk'
database='/storage/brno3-cerit/home/kika/databases/MMETSP_uniclust50_MERC/MMETSP_uniclust50_MERC_profiles'

#copy files to scratch
cp $data_dir'5-tiara/eukarya_P3S_scaffolds.fasta' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

contigs='eukarya_P3S_scaffolds.fasta'
out='euk_metaeuk'

$metaeuk easy-predict --threads $PBS_NUM_PPN $contigs $database $out $SCRATCHDIR

#copy files back
rm $contigs
cp -r * $data_dir'6-metaeuk_profiles/'
