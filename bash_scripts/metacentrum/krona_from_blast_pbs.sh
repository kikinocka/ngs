#!/bin/bash
#PBS -N krona
#PBS -l select=1:ncpus=20:mem=5gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add krona-2.8.1

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/20200821_BML-P3B/'
taxonomy='/storage/brno3-cerit/home/kika/databases/krona/'

#copy files to scratch
cp $datadir'euk_metaeuk.blast_upd.out' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

blast='euk_metaeuk.blast_upd.out'
krona='euk_metaeuk.blast_upd.krona.html'

ktImportBLAST $blast -o $krona -tax $taxonomy


#copy files back
rm $blast
cp -R * $datadir