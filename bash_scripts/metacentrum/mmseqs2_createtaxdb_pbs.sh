#!/bin/bash
#PBS -N mmseqs2
#PBS -l select=1:ncpus=10:mem=20gb:scratch_local=30gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

mmseqs='/storage/brno3-cerit/home/kika/miniconda3/bin/mmseqs'
data_dir='/storage/brno3-cerit/home/kika/databases/eukprot/'
ncbi=$data_dir'ncbi-taxdump'

#copy files to scratch
cp $data_dir'eukprot' $SCRATCHDIR
cp $data_dir'eukprot.taxidmapping' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

database='eukprot'
taxidmapping='eukprot.taxidmapping'

$mmseqs createtaxdb $database tmp --ncbi-tax-dump $ncbi --tax-mapping-file $taxidmapping --threads $PBS_NUM_PPN

#copy files back
rm $database
cp -r * $data_dir
