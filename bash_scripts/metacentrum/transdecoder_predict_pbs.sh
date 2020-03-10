#!/bin/bash
#PBS -N TransDecoder_Predict
#PBS -l select=1:ncpus=10:mem=10gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add hmmer-3.2
module add transdecoder-3.0.1

data_dir='/storage/brno3-cerit/home/kika/diplonemids/trafficking/'
# pfam_dir='/storage/brno3-cerit/home/kika/pfam/'

#copy files to scratch
# cp $pfam_dir'Pfam-A.hmm' $SCRATCHDIR
cp $data_dir'rhRABs.fwd_hits.fa' $SCRATCHDIR
# cp -r $data_dir'pelomyxa_transcriptome_clean.fa.transdecoder_dir' $SCRATCHDIR
cp $data_dir'rhRABs_rev.blastx.out' $SCRATCHDIR

# hmm='Pfam-A.hmm'
transcriptome='rhRABs.fwd_hits.fa'
blast='rhRABs_rev.blastx.out'
# orfs='pelomyxa_transcriptome_clean.fa.transdecoder_dir/longest_orfs.pep'


#compute on scratch
cd $SCRATCHDIR
# hmmpress $hmm
# hmmscan --cpu $PBS_NUM_PPN --domtblout pfam.domtblout $hmm $orfs
TransDecoder.Predict -t $transcriptome --retain_blastp_hits $blast #--retain_pfam_hits pfam.domtblout


#copy files back
# rm -r $transcriptome $hmm 'pelomyxa_transcriptome_clean.fa.transdecoder_dir/'
# cp -r * $data_dir'pelomyxa_transcriptome_clean.fa.transdecoder_dir/'
rm $transcriptome $blast
cp -r * $data_dir
