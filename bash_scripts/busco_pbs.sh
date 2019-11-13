#!/bin/sh
#PBS -N BUSCO
#PBS -q default
#PBS -l select=1:ncpus=1:mem=1gb:scratch_local=10gb:os=debian9
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add busco-3.0.2
module add augustus-3.3.1

#setting augustus config file environment variable
augustus_configs='/storage/brno3-cerit/home/kika/augustus_configs/'
mkdir $SCRATCHDIR/augustus_configs/
cp -r $augustus_configs/* $SCRATCHDIR/augustus_configs/ || exit 1
export AUGUSTUS_CONFIG_PATH=$SCRATCHDIR/augustus_configs
export PATH=$PATH:/software/augustus/3.3.1/src/bin:/software/augustus/3.3.1/src/scripts

# assembly_dir='/storage/brno3-cerit/home/kika/sags/reassembly/spades/'
# lin_dir='/software/busco/3.0.2/src/db/'
# busco_dir='/storage/brno3-cerit/home/kika/sags/reassembly/reports/busco/'
sumaries='/storage/brno3-cerit/home/kika/sags/reassembly/reports/busco/sumaries/'

#copy files to scratch
# cp $assembly_dir'contigs.fasta' $SCRATCHDIR
# cp -r $lin_dir'protists_ensembl/' $SCRATCHDIR
cp $sumaries'*' $SCRATCHDIR

# assembly='contigs.fasta'
# base='protists_ensembl'
# lineage='protists_ensembl/'
# mode='genome'
# species='toxoplasma'


#compute on scratch
cd $SCRATCHDIR
# run_BUSCO.py -i $assembly -o $base -l $lineage -m $mode -c $PBS_NUM_PPN -sp $species
 generate_plot.py -wd $sumaries

#copy files back
# rm -r $assembly $lineage augustus_configs
# cp -r * $busco_dir
rm short_summary*
cp -r * $sumaries
