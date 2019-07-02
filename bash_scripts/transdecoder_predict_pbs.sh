#!/bin/bash
#PBS -N TransDecoder_Predict
#PBS -l select=1:ncpus=10:mem=10gb:scratch_local=50gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add hmmer-3.2
module add transdecoder-3.0.1

data_dir='/storage/brno3-cerit/home/kika/pelomyxa/transcriptome_assembly/'
pfam_dir='/storage/brno3-cerit/home/kika/pfam/'

#copy files to scratch
cp $pfam_dir'Pfam-A.hmm' $SCRATCHDIR

cp $data_dir'pelomyxa_transcriptome_clean.fa' $SCRATCHDIR
cp -r $data_dir'pelomyxa_transcriptome_clean.fa.transdecoder_dir' $SCRATCHDIR

hmm='Pfam-A.hmm'
transcriptome='pelomyxa_transcriptome_clean.fa'
orfs='pelomyxa_transcriptome_clean.fa.transdecoder_dir/longest_orfs.pep'


#compute on scratch
cd $SCRATCHDIR
hmmpress $hmm
hmmscan --cpu $PBS_NUM_PPN --domtblout pfam.domtblout $hmm $orfs
TransDecoder.Predict -t $transcriptome --retain_blastp_hits pfam.domtblout


#copy files back
cd $transcriptome $hmm
cp -r * $data_dir'pelomyxa_transcriptome_clean.fa.transdecoder_dir/'
# cp pfam.domtblout $data_dir'pelomyxa_transcriptome_clean.fa.transdecoder_dir/'
# cp pelomyxa_transcriptome_clean.fa.transdecoder.* $data_dir'pelomyxa_transcriptome_clean.fa.transdecoder_dir/'
