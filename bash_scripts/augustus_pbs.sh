#!/bin/sh
#PBS -N Augustus
#PBS -q default
#PBS -l select=1:ncpus=1:mem=1gb:scratch_local=10gb:os=debian9
#PBS -l walltime=0:02:00
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

#copy files to scratch
datadir='/storage/brno3-cerit/home/kika/pelomyxa/augustus/'

#augustus runs on 1 core only
cd $SCRATCHDIR

# #1) SPLIT GENES
# cp $datadir'augustus_dataset_deduplicated.gb' $SCRATCHDIR
# randomSplit.pl augustus_dataset_deduplicated.gb 100
# rm augustus_dataset_deduplicated.gb

# #2) CREATE A META PARAMETERS FILE
# new_species.pl --species=pelomyxa
# mkdir $augustus_configs/pelomyxa
# cp -r $SCRATCHDIR/augustus_configs/species/pelomyxa/* $augustus_configs/pelomyxa/.

# #3) MAKE AN INITIAL TRAINING
# cp $datadir'augustus_dataset_deduplicated.gb.train' $SCRATCHDIR
# etraining --species=pelomyxa augustus_dataset_deduplicated.gb.train
# cp -r $SCRATCHDIR/augustus_configs/species/pelomyxa/* $augustus_configs/species/pelomyxa/.
# rm augustus_dataset_deduplicated.gb.train

cp $datadir'augustus_dataset_deduplicated.gb.test' $SCRATCHDIR
augustus --species=pelomyxa augustus_dataset_deduplicated.gb.test | tee pelo_first_test.out
cp pelo_first_test.out $datadir

# #4) OPTIMIZE AUGUSTUS
# cp $datadir'augustus_dataset_deduplicated.gb.train' $SCRATCHDIR
# optimize_augustus.pl --species=pelomyxa augustus_dataset_deduplicated.gb.train --cpus=$PBS_NUM_PPN
# rm augustus_dataset_deduplicated.gb.train

rm -r augustus_configs
cp -r * $datadir || export CLEAN_SCRATCH=false
