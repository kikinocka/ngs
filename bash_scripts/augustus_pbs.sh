#!/bin/sh
#PBS -N Augustus
#PBS -q default
#PBS -l select=1:ncpus=1:mem=5gb:scratch_local=30gb:os=debian9
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add augustus-3.3.1

#setting augustus config file environment variable
augustus_configs='/storage/brno3-cerit/home/kika/augustus_configs/'
mkdir $SCRATCHDIR/augustus_configs/
cp -r $augustus_configs/* $SCRATCHDIR/augustus_configs/ || exit 1
export AUGUSTUS_CONFIG_PATH=$SCRATCHDIR/augustus_configs
export PATH=$PATH:/software/augustus/3.3.1/src/bin:/software/augustus/3.3.1/src/scripts

datadir='/storage/brno3-cerit/home/kika/pelomyxa/augustus/'

#augustus runs on 1 core only
cd $SCRATCHDIR

# #1) CONVERT GFF FILE TO GENBANK (1 min, 250 MB)
# cp $datadir'pelo_final.corrected.gff' $SCRATCHDIR
# cp /storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/pelomyxa_final_genome.fa $SCRATCHDIR
# gff2gbSmallDNA.pl pelo_final.corrected.gff pelomyxa_final_genome.fa 60 pelo_final.corrected.gb
# rm pelomyxa_final_genome.fa pelo_final.corrected.gff

# #2) SPLIT GENES - may be skipped if not enough gene models available
# cp $datadir'pelo_final_strict.gb' $SCRATCHDIR
# randomSplit.pl pelo_final_strict.gb 100
# rm pelo_final_strict.gb

# #3) CREATE A META PARAMETERS FILE
# new_species.pl --species=pelomyxa
# mkdir $augustus_configs/pelomyxa
# cp -r $SCRATCHDIR/augustus_configs/species/pelomyxa/* $augustus_configs/pelomyxa/.

# #4) MAKE AN INITIAL TRAINING (1 min, 150 MB)
# cp $datadir'pelo_final.corrected.gb' $SCRATCHDIR
# etraining --species=pelomyxa pelo_final.corrected.gb
# cp -r $SCRATCHDIR/augustus_configs/species/pelomyxa/* $augustus_configs/species/pelomyxa/.
# rm pelo_final.corrected.gb

# #not run if 2) is skipped
# cp $datadir'pelo_final.gb.test' $SCRATCHDIR
# augustus --species=pelomyxa pelo_final.gb.test | tee pelo_first_test.out
# cp pelo_first_test.out $datadir

# #5) OPTIMIZE AUGUSTUS (~ 1h, 150 MB)
# cp $datadir'pelo_final.corrected.gb' $SCRATCHDIR
# optimize_augustus.pl --species=pelomyxa --cpus=$PBS_NUM_PPN pelo_final.corrected.gb
# cp -r $SCRATCHDIR/augustus_configs/species/pelomyxa/* $augustus_configs/species/pelomyxa/.
# rm pelo_final.corrected.gb

# #6) RETRAIN AUGUSTUS (2 min, 150 MB)
# cp $datadir'pelo_final.corrected.gb' $SCRATCHDIR
# etraining --species=pelomyxa pelo_final.corrected.gb
# cp -r $SCRATCHDIR/augustus_configs/species/pelomyxa/* $augustus_configs/species/pelomyxa/.
# rm pelo_final.corrected.gb

#7) PREDICT GENES
cp '/storage/brno3-cerit/home/kika/pelomyxa/genome_assembly/pelomyxa_final_genome.fa' $SCRATCHDIR
cp $datadir'accepted_hits.introns.gff' $SCRATCHDIR
genome='pelomyxa_final_genome.fa'
introns='accepted_hits.introns.gff'
out='pelo_augustus.gff'

augustus --extrinsicCfgFile= --species=pelomyxa --hintsfile=$introns \
--allow_hinted_splicesites=atac --protein=on --gff3=on --genemodel=complete --progress=true \
--min_intron_len=30 --outfile=$out $genome
rm $genome
rm $introns

# augustus --extrinsicCfgFile=../hints/extrinsic.cfg --species=Streblomastix --hintsfile=../hints/hints.2.gff \
# --allow_hinted_splicesites=atac --protein=on --gff3=on --genemodel=partial --progress=true \
# --outfile=Streblomastix_predicted_protein.gff --min_intron_len=25 \
# /home/sebastian/Streblomastix/eukaryote/final_work/renaming/Streblomastix_genome_final.fasta

#copy files back
rm -r augustus_configs
cp -r * $datadir || export CLEAN_SCRATCH=false
