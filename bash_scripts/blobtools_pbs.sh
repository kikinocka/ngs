#!/bin/bash
#PBS -N blobtools
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blobtools-1.0

#copy files to scratch
cd /storage/brno3-cerit/home/fussyz01/DMND/
cp prot_ryby.accession2taxid $SCRATCHDIR/prot.accession2taxid

cd /storage/brno3-cerit/home/kika/pelomyxa/transcriptome_assembly/
cp blobtools/pelo_trinity_dmnd_bx.out $SCRATCHDIR
cp pelomyxa_trinity.fa $SCRATCHDIR


transcriptome='pelomyxa_trinity.fa'
dmnd='pelo_trinity_dmnd_bx.out'
taxmap='prot.accession2taxid'
sam=''

#compute on scratch
cd $SCRATCHDIR

blobtools taxify -f $dmnd -m $taxmap -s 1 -t 2
blobtools create -i $transcriptome -s $sam -t ryba_sterling.taxified.out -o blobdb
blobtools view -i blobdb.blobDB.json -o plots
blobtools plot -i blobdb.blobDB.json -o order

#copy files back
cp  || export CLEAN_SCRATCH=false
