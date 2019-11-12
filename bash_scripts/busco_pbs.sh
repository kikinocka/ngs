#!/bin/sh
#PBS -N BUSCO
#PBS -q default
#PBS -l select=1:ncpus=1:mem=15gb:scratch_local=10gb:os=debian9
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

#add module
module add busco-3.0.2
module add augustus-3.3.1

#setting augustus config file environment variable
augustus_configs='/storage/brno3-cerit/home/kika/augustus_configs/'
mkdir $SCRATCHDIR/augustus_configs/
cp -r $augustus_configs/* $SCRATCHDIR/augustus_configs/ || exit 1
export AUGUSTUS_CONFIG_PATH=$SCRATCHDIR/augustus_configs
export PATH=$PATH:/software/augustus/3.3.1/src/bin:/software/augustus/3.3.1/src/scripts

BUSCO_DB=eukaryota_odb9
assembly_dir='/storage/brno3-cerit/home/kika/sags/reassembly/spades/'
lin_dir='/software/busco/3.0.2/src/db/'
busco_dir='/storage/brno3-cerit/home/kika/sags/reassembly/reports/busco/'

#copy files to scratch
cp $data_dir'contigs.fasta' $SCRATCHDIR

assembly='contigs.fasta'
base='eukaryota_odb9'
mode='genome'
species='fly'


#compute on scratch
cd $SCRATCHDIR
python run_BUSCO.py -i $assembly -o $base -l $BUSCO_DB -m $mode -c $PBS_NUM_PPN -sp $species

#copy files back
rm $assembly $augustus_configs
cp -r * $busco_dir
