#!/bin/sh
#PBS -N BUSCO
#PBS -q default
#PBS -l select=1:ncpus=3:mem=1gb:scratch_local=10gb:os=debian9
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

assembly_dir='/storage/brno3-cerit/home/kika/archamoebae/'
busco_dir=$assembly_dir'busco/'
# lin_dir='/software/busco/3.0.2/src/db/'

sumaries=$busco_dir'sumaries/'
ln -s $busco_dir'mab_eukaryota_odb9/short_summary_eukaryota_odb9.txt' $sumaries
ln -s $busco_dir'mei_eukaryota_odb9/short_summary_eukaryota_odb9.txt' $sumaries
ln -s $busco_dir'psp_eukaryota_odb9/short_summary_eukaryota_odb9.txt' $sumaries
ln -s $busco_dir'rel_eukaryota_odb9/short_summary_eukaryota_odb9.txt' $sumaries
ln -s $busco_dir'rli_eukaryota_odb9/short_summary_eukaryota_odb9.txt' $sumaries

# copy files to scratch
# cp $assembly_dir'rli_trinity_010416_renamed_nucl.fasta' $SCRATCHDIR
# cp -r $lin_dir'eukaryota_odb9/' $SCRATCHDIR

# assembly='rli_trinity_010416_renamed_nucl.fasta'
# base='eukaryota_odb9'
# lineage='eukaryota_odb9/'
# mode='transcriptome'


#compute on scratch
cd $SCRATCHDIR
# run_BUSCO.py -i $assembly -o $base -l $lineage -m $mode -c $PBS_NUM_PPN
generate_plot.py -wd $sumaries

#copy files back
# rm -r $assembly $lineage augustus_configs
# cp -r * $busco_dir
cp -r * $sumaries
