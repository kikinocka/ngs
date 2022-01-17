#!/bin/bash
#PBS -N mmseqs2
#PBS -l select=1:ncpus=10:mem=100gb:scratch_local=30gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

mmseqs='/storage/brno3-cerit/home/kika/miniconda3/bin/mmseqs'
db_dir='/storage/brno3-cerit/home/kika/databases/eukprotDB'
data_dir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/P1B_1-05C_L001-ds.ec8b691bd68b44deb59919ca3da275ba/'

#copy files to scratch
cp $db_dir'/'* $SCRATCHDIR
cp $data_dir'6-metaeuk/profiles/euk_metaeuk.fas' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

database='eukprotDB'
query='euk_metaeuk.fas'
queryDB='euk_metaeukDB'
taxonomy='euk_metaeuk.tax'
taxres=$taxonomy'.tsv'
report=$taxonomy'.html'

$mmseqs createdb $query $queryDB

$mmseqs taxonomy $queryDB $database $taxonomy tmp --threads $PBS_NUM_PPN
$mmseqs createtsv $queryDB $taxonomy $taxres --threads $PBS_NUM_PPN
$mmseqs taxonomyreport $database $taxonomy $report --report-mode 1 --threads $PBS_NUM_PPN
#--report-mode INT   Taxonomy report mode 0: Kraken 1: Krona [0]

#copy files back
rm -r $query tmp eukprotDB*
cp -r * $data_dir'9-mmseqs2'
