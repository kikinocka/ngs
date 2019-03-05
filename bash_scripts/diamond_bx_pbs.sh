#!/bin/bash
#PBS -N Diamond-bx
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add diamond-0.8.28


#copy files to scratch
cd /storage/brno3-cerit/home/fussyz01/DMND/
cp refseq_ryby.dmnd $SCRATCHDIR/refseq.dmnd
cp prot_ryby.accession2taxid $SCRATCHDIR/prot.accession2taxid

cd /storage/brno3-cerit/home/kika/pelomyxa/transcriptome_assembly/
cp pelomyxa_trinity.fa $SCRATCHDIR

query='pelomyxa_trinity.fa'
db='refseq.dmnd'
taxmap='prot.accession2taxid'
out='pelo_trinity_dmnd_bx.out'


#compute on scratch
cd $SCRATCHDIR

diamond blastx -q $query -d $db -o $out --taxonmap $taxmap -p $PBS_NUM_PPN -f 6 qseqid staxids bitscore --sensitive --max-target-seqs 1 --evalue 1e-5

#copy files back
cp $out /storage/brno3-cerit/home/kika/pelomyxa/transcriptome_assembly/. || export CLEAN_SCRATCH=false
