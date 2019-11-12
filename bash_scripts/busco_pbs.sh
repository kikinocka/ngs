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

assembly_dir='/storage/brno3-cerit/home/kika/sags/reassembly/spades/'
lin_dir='/software/busco/3.0.2/src/db/'
busco_dir='/storage/brno3-cerit/home/kika/sags/reassembly/reports/busco/'

#copy files to scratch
cp $data_dir'contigs.fasta' $SCRATCHDIR
cp -r $lin_dir'eukaryota_odb9/' $SCRATCHDIR

assembly='contigs.fasta'
lineage='eukaryota_odb9/'
base='eukaryota_odb9'
mode='genome'
species='fly'


#compute on scratch
cd $SCRATCHDIR
run_BUSCO.py -i $assembly -o base -l $lineage -m $mode -c $PBS_NUM_PPN -sp $species
