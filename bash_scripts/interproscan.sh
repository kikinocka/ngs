#!/bin/sh
#PBS -N InterProScan
#PBS -q default
#PBS -l select=1:ncpus=10:mem=50gb:scratch_local=50gb
#PBS -l walltime=4:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add interproscan-5.20-59.0

datadir='/storage/brno3-cerit/home/kika/elonga/'

#copy files to scratch
cp $datadir'EL_hits_aa.fa' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

interproscan.sh -dp -f TSV,GFF3 -T $SCRATCHDIR -i EL_hits_aa.fa -b EL_hits_interpro -appl PRINTS,Pfam,Hamap,ProSitePatterns,ProSiteProfiles,Panther -goterms --pathways -iprlookup

#copy files back
rm EL_hits_aa.fa
cp -r * $datadir
