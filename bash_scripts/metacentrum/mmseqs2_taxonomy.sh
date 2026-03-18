#!/bin/bash
#PBS -N mmseqs2
#PBS -l select=1:ncpus=10:mem=100gb:scratch_local=30gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

mmseqs='/storage/brno3-cerit/home/kika/miniconda3/bin/mmseqs'
db_dir='/storage/brno12-cerit/home/kika/databases/eukprot_v3_DB/'
data_dir='/storage/brno12-cerit/home/kika/cz-au_fire/'

#copy files to scratch
cp $db_dir'eukprot_v3_DB'* $SCRATCHDIR
cp $data_dir'3-metaeuk/eukarya_metaeuk.fas' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

database='eukprot_v3_DB'
query='eukarya_metaeuk.fas'
queryDB='eukarya_metaeuk'
taxonomy='eukarya_metaeuk.tax'
table=$taxonomy'.tsv'
krona=$taxonomy'.html'

$mmseqs createdb $query $queryDB

$mmseqs taxonomy $queryDB $database $taxonomy tmp --threads $PBS_NUM_PPN
$mmseqs createtsv $queryDB $taxonomy $table --threads $PBS_NUM_PPN
$mmseqs taxonomyreport $database $taxonomy $krona --report-mode 1 --threads $PBS_NUM_PPN
#--report-mode INT   Taxonomy report mode 0: Kraken 1: Krona [0]

#copy files back
rm -r $query $database* tmp
cp -r * $data_dir'4-mmseqs2'
