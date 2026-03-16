#!/bin/bash
#PBS -N metaeuk
#PBS -l select=1:ncpus=50:mem=500gb:scratch_local=300gb
#PBS -l walltime=336:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

# #Metaeuk installation
# module add mambaforge
# mamba create --prefix /storage/brno12-cerit/home/kika/metaeuk_env -y
# mamba activate /storage/brno12-cerit/home/kika/metaeuk_env
# mamba install -c conda-forge -c bioconda metaeuk
# mamba deactivate

data_dir='/storage/brno12-cerit/home/kika/cz-au_fire/'
# metaeuk='/storage/brno3-cerit/home/kika/miniconda3/bin/metaeuk'
db_dir='/storage/brno3-cerit/home/kika/databases/MMETSP_uniclust50_MERC/'

#copy files to scratch
cp $data_dir'whokaryote_out/eukaryotes.fasta' $SCRATCHDIR
cp $db_dir'MMETSP_uniclust50_MERC'* $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
module add mambaforge
mamba create -p $SCRATCHDIR/metaeuk_env --clone /storage/brno12-cerit/home/kika/metaeuk_env
mamba activate $SCRATCHDIR/metaeuk_env

database='MMETSP_uniclust50_MERC'
contigs='eukaryotes.fasta'
out='eukarya_metaeuk'

metaeuk easy-predict --threads $PBS_NUM_PPN $contigs $database $out $SCRATCHDIR
mamba deactivate

#copy files back
rm -r $contigs $database metaeuk_env
cp -r * $data_dir'metaeuk/'
