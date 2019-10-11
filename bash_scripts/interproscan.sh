#!/bin/sh
#PBS -N InterProScan
#PBS -q default
#PBS -l select=1:ncpus=10:mem=5gb:scratch_local=50gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add interproscan-5.20-59.0

datadir='/storage/brno3-cerit/home/kika/pelomyxa/predicted_proteins_transdecoder/'

#copy files to scratch
cp $datadir'pelo.mit_predicted.fa' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
input='pelo.mit_predicted.fa'
out='pelo.mit_predicted.interpro'

interproscan.sh -dp -f TSV,GFF3 -T $SCRATCHDIR -i $input -b $out -appl PRINTS,Pfam,Hamap,ProSitePatterns,ProSiteProfiles,Panther -goterms --pathways -iprlookup

#copy files back
rm $input
cp -r * $datadir
