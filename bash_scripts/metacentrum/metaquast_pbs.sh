#!/bin/bash
#PBS -N metaquast
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=20gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.8.0a
module add quast-4.6.3

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenome/'

#copy files to scratch
cp $datadir'bml_eukaryotes.spades_reassembly.fa' $SCRATCHDIR
cp $datadir'bw2_mapping/eukaryotes_prokka/bml_euk_prokka_bw2_mapped.fq.1.gz' $SCRATCHDIR
cp $datadir'bw2_mapping/eukaryotes_prokka/bml_euk_prokka_bw2_mapped.fq.2.gz' $SCRATCHDIR

metagenome='bml_eukaryotes.spades_reassembly.fa'
fwd='bml_euk_prokka_bw2_mapped.fq.1.gz'
rev='bml_euk_prokka_bw2_mapped.fq.2.gz'


#compute on scratch
cd $SCRATCHDIR
metaquast.py -o $SCRATCHDIR -t $PBS_NUM_PPN -1 $fwd -2 $rev $metagenome


#copy results to your folder
rm $metagenome $fwd $rev
cp -r * $datadir'metaquast/eukaryotes_reassembly/'
