#!/bin/bash
#PBS -N TransDecoder_Predict
#PBS -l select=1:ncpus=10:mem=20gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add hmmer-3.2
module add transdecoder-3.0.1

data_dir='/storage/brno3-cerit/home/kika/pelomyxa/transcriptome_assembly/'
pfam_dir='/auto/brno3-cerit/nfs4/home/kika/pfam/'

#copy files to scratch
cd $pfam_dir
cp Pfam-A.hmm $SCRATCHDIR

cd $data_dir
cp pelomyxa_trinity.fa $SCRATCHDIR
cp pelomyxa_trinity.fa.transdecoder_dir/longest_orfs.pep $SCRATCHDIR

hmm='Pfam-A.hmm'
transcriptome='pelomyxa_trinity.fa'
orfs='longest_orfs.pep'

#compute on scratch
cd $SCRATCHDIR
hmmpress $hmm
hmmscan --cpu $PBS_NUM_PPN --domtblout pfam.domtblout $hmm $orfs
TransDecoder.Predict -t $transcriptome --retain_blastp_hits pfam.domtblout

#copy files back
rm $transcriptome $hmm $orfs
cp -r * $data_dir'pelomyxa_trinity.fa.transdecoder_dir/'
