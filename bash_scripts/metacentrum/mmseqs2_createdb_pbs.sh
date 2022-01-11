#!/bin/bash
#PBS -N mmseqs2
#PBS -l select=1:ncpus=10:mem=20gb:scratch_local=30gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

mmseqs='/storage/brno3-cerit/home/kika/miniconda3/bin/mmseqs'
data_dir='/storage/brno3-cerit/home/kika/databases/'
ncbi=$data_dir'ncbi-taxdump'

#copy files to scratch
cp $data_dir'eukprot_v2_proteins_renamed.taxids.faa' $SCRATCHDIR
cp $data_dir'eukprot.taxidmapping' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

fasta='eukprot_v2_proteins_renamed.taxids.faa'
database='eukprotDB'
taxidmapping='eukprot.taxidmapping'

$mmseqs createdb $fasta $database
$mmseqs createtaxdb $database tmp --ncbi-tax-dump $ncbi --tax-mapping-file $taxidmapping --threads $PBS_NUM_PPN

#copy files back
rm -r $fasta $taxidmapping tmp
cp -r * $data_dir'eukprotDB'
