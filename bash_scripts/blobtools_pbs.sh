#!/bin/bash
#PBS -N blobtools
#PBS -l select=1:ncpus=1:mem=80gb:scratch_local=50gb
#PBS -l walltime=15:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blobtools-1.0

pelo_dir='/storage/brno3-cerit/home/kika/pelomyxa/'
data_dir=$pelo_dir'transcriptome_assembly/'
mapping_dir=$pelo_dir'mapping/bowtie2/RNA_to_transcriptome/pelo_clean/'
blob_dir='/storage/brno3-cerit/home/kika/blobtools/'

#copy files to scratch
cp $data_dir'pelomyxa_transcriptome_clean.fa' $SCRATCHDIR
cp $mapping_dir'pelo_trinity_clean_bw2.sam' $SCRATCHDIR
cp $data_dir'blobtools/pelo_clean/pelo_clean_dmnd_bx.out' $SCRATCHDIR
cp $blob_dir'prot.accession2taxid' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR

transcriptome='pelomyxa_transcriptome_clean.fa'
sam='pelo_trinity_clean_bw2.sam'
dmnd='pelo_clean_dmnd_bx.out'
taxid='prot.accession2taxid'
taxified='pelo_clean_dmnd_bx.taxified.out'
base='blobDB'
rank='superkingdom'

blobtools taxify -f $dmnd -m $taxid -s 1 -t 2
blobtools create -i $transcriptome -s $sam -t $taxified -o $base
blobtools view -i $base'.blobDB.json' --cov -o table
blobtools plot -i $base'.blobDB.json' -r $rank -o plot 

#copy files back
rm $transcriptome $sam $dmnd $taxid
cp -r * $data_dir'blobtools/pelo_clean/' || export CLEAN_SCRATCH=false
