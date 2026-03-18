#!/bin/bash
#PBS -N mmseqs2
#PBS -l select=1:ncpus=10:mem=20gb:scratch_local=30gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

mmseqs='/storage/brno3-cerit/home/kika/miniconda3/bin/mmseqs'
data_dir='/storage/brno3-cerit/home/kika/databases/'

#copy files to scratch
cp $data_dir'eukprot_v3.faa' $SCRATCHDIR
cp $data_dir'eukprot_v3.taxidmapping' $SCRATCHDIR
cp -r $data_dir'ncbi_taxdump' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

fasta='eukprot_v3.faa'
mapping='eukprot_v3.taxidmapping'
ncbi='ncbi_taxdump'
database='eukprot_v3_DB'

$mmseqs createdb $fasta $database
$mmseqs createtaxdb $database tmp --ncbi-tax-dump $ncbi --tax-mapping-file $mapping --threads $PBS_NUM_PPN

#copy files back
rm -r $fasta $mapping $ncbi tmp
cp -r * $data_dir'eukprot_v3_DB'
