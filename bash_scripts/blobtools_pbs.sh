#!/bin/bash
#PBS -N blobtools
#PBS -l select=1:ncpus=1:mem=80gb:scratch_local=50gb
#PBS -l walltime=48:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blobtools-1.0

#copy files to scratch
cd /storage/brno3-cerit/home/kika/blobtools/
cp prot.accession2taxid $SCRATCHDIR

cd /storage/brno3-cerit/home/kika/pelomyxa/transcriptome_assembly/
cp blobtools/pelo_trinity_dmnd_bx.out $SCRATCHDIR/pelo_trinity.out
cp pelomyxa_trinity.fa $SCRATCHDIR

cd /storage/brno3-cerit/home/kika/pelomyxa/mapping/bowtie2/RNA_to_transcriptome/
cp pelo_trinity_bw2.sam $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

transcriptome='pelomyxa_trinity.fa'
dmnd='pelo_trinity.out'
taxmap='prot.accession2taxid'
sam='pelo_trinity_bw2.sam'
taxified='pelo_trinity.taxified.out'
base='blobDB'

blobtools taxify -f $dmnd -m $taxmap -s 0 -t 1
blobtools create -i $transcriptome -s $sam -t $taxified -o $base
blobtools view -i $base'.blobDB.json' --cov -o table
blobtools plot -i $base'.blobDB.json' -o plot 

#copy files back
rm $transcriptome $dmnd $taxmap $sam 
cp -r * /storage/brno3-cerit/home/kika/pelomyxa/transcriptome_assembly/blobtools/. || export CLEAN_SCRATCH=false
