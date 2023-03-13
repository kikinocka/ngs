#!/bin/sh
#PBS -N InterProScan
#PBS -q default
#PBS -l select=1:ncpus=10:mem=5gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add interproscan-5.55-88.0

datadir='/storage/brno3-cerit/home/kika/blasto_comparative/proteins_obscuro'

#copy files to scratch
# cp $datadir'/'*.faa $SCRATCHDIR
cp $datadir'/Ovol_companion.l30.faa' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for fasta in *.faa; do
	echo $fasta
	out=${fasta%.faa}.interpro
	interproscan.sh -dp -f TSV,GFF3 -T $SCRATCHDIR -cpu $PBS_NUM_PPN -i $fasta -b $out -appl Pfam -goterms --pathways -iprlookup
	# -appl PRINTS,Pfam,Hamap,ProSitePatterns,ProSiteProfiles,Panther 
done

#copy files back
rm *.faa
cp -r * $datadir
