#!/bin/bash
#PBS -N diamond-bx
#PBS -l select=1:ncpus=20:mem=50gb:scratch_local=50gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add diamond-0.8.29

#copy files to scratch
cd /storage/brno3-cerit/home/fussyz01/DMND/
cp refseq_ryby.dmnd $SCRATCHDIR/refseq.dmnd

cd /storage/brno3-cerit/home/kika/pelomyxa/transcriptome_assembly/
cp pelomyxa_trinity.fa $SCRATCHDIR

query='pelomyxa_trinity.fa'
db='refseq.dmnd'
out='pelo_trinity_dmnd_bx.out'


#compute on scratch
cd $SCRATCHDIR

diamond blastx -q $query -d $db -o $out -p $PBS_NUM_PPN -f 6 --sensitive --max-target-seqs 1 --evalue 1e-5

#copy files back
cp $out /storage/brno3-cerit/home/kika/pelomyxa/transcriptome_assembly/. || export CLEAN_SCRATCH=false
