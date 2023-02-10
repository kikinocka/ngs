#!/bin/sh
#PBS -N InterProScan
#PBS -q default
#PBS -l select=1:ncpus=10:mem=5gb:scratch_local=50gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add interproscan-5.55-88.0

datadir='/storage/brno3-cerit/home/kika/pelomyxa/predicted_proteins_transdecoder/'

#copy files to scratch
cp $datadir'bnon_nohit.fa' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
input='bnon_nohit.fa'
out='bnon_nohit.interpro.out'

interproscan.sh -dp -f TSV,GFF3 -T $SCRATCHDIR -cpu $PBS_NUM_PPN -i $input -b $out -appl Pfam -goterms --pathways -iprlookup
# -appl PRINTS,Pfam,Hamap,ProSitePatterns,ProSiteProfiles,Panther 

#copy files back
rm $input
cp -r * $datadir
