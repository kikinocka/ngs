#!/bin/bash
#PBS -N whokaryote
#PBS -l select=1:ncpus=20:mem=100gb:scratch_local=50gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

# #Whokaryote installation
# module add mambaforge
# mamba create --prefix /storage/brno12-cerit/home/kika/whokaryote_env -y
# mamba activate /storage/brno12-cerit/home/kika/whokaryote_env
# mamba install -c bioconda whokaryote
# mamba deactivate

datadir='/storage/brno12-cerit/home/kika/cz-au_fire/'

#copy files to scratch
cp $datadir'contigs_fixlabel.fasta' $SCRATCHDIR
echo '------------------'
echo 'copying files done'
echo '------------------'

#compute on scratch
cd $SCRATCHDIR
module add mambaforge
mamba create -p $SCRATCHDIR/whokaryote_env --clone /storage/brno12-cerit/home/kika/whokaryote_env
mamba activate $SCRATCHDIR/whokaryote_env

echo '------------------------------'
echo 'mamba env copied and activated'
echo '------------------------------'

echo '-------------------'
echo 'starting Whokaryote'
echo '-------------------'

metagenome='contigs_fixlabel.fasta'
size=3000
mkdir whokaryote_out
whokaryote.py --contigs $metagenome --outdir whokaryote_out --f --minsize $size --threads $PBS_NUM_PPN
# --contigs CONTIGS  The path to your contigs file. It should be one (multi)fasta (DNA).
# --outdir OUTDIR    Specify the path to your preferred output directory. No / at the end.
# --gff GFF          If you already have gene predictions, specify path to the .gff file
# --f                If you want new multifastas with only eukaryotes and only prokaryotes.
# --test             If you want to test it on a known dataset.
# --train TRAIN      For training an RF on your own dataset. Provide name of RF output file.
# --minsize MINSIZE  Select a minimum contig size in bp, default = 5000. Accuracy on contigs below 5000 is lower.
# --model MODEL      Choose the stand-alone model or the tiara-integrated model: S or T. Option 'T' only works with argument --contigs
# --threads THREADS  Number of threads for Tiara to use.
#If you don't specify --model, it will run the model that integrates Tiara predictions.
mamba deactivate

#copy files back
rm -r $metagenome whokaryote_env
cp -r * $datadir

