#!/bin/bash
#PBS -N aragorn
#PBS -l select=1:ncpus=1:mem=1gb:scratch_local=5gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

aragorn='/storage/brno3-cerit/home/kika/miniconda3/pkgs/aragorn-1.2.38-h779adbc_4/bin/aragorn'
data_dir='/storage/brno3-cerit/home/kika/tRNAs-kinetoplastids/'

#copy files to scratch
cp $data_dir'TriTrypDB-55_TbruceiLister427_Genome.fasta' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

genome='TriTrypDB-55_TbruceiLister427_Genome.fasta'
out='TriTrypDB-55_TbruceiLister427_Genome.aragorn.fa'

$aragorn -t -fo -o $out $genome


#copy files back
rm $genome
cp * $data_dir