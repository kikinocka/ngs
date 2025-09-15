#!/bin/sh
#PBS -N InterProScan
#PBS -q default
#PBS -l select=1:ncpus=10:mem=5gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add interproscan

datadir='/storage/brno12-cerit/home/kika/kinetoplastids/lmaj_virulence/'

#copy files to scratch
cp $datadir'lmaj_DGE_all.fa' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for fasta in *.fa; do
	echo $fasta
	out=${fasta%.faa}.interpro
	interproscan.sh -dp -f TSV,GFF3 -T $SCRATCHDIR -cpu $PBS_NUM_PPN -i $fasta -b $out -goterms --pathways -iprlookup
	#-f TSV,GFF3
	#-appl PRINTS,Pfam,Hamap,ProSitePatterns,ProSiteProfiles,Panther 
done

#copy files back
rm *.fa
cp -r * $datadir
