#!/bin/sh
#PBS -N BUSCO_retortamonas_genomic
#PBS -q default
#PBS -l select=1:ncpus=1:mem=16gb:scratch_local=10gb:os=debian9
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

trap 'clean_scratch' TERM EXIT

module add busco-3.0.2
module add augustus-3.3.1
# module add samtools-1.9
# module add blast+-2.6.0
# module add hmmer-3.1b1-gcc - hmmer added with Augustus, no need for another

# how to set augustus config file environment variable example
#mkdir $SCRATCHDIR/augustus_configs
#
#export AUGUSTUS_CONFIG_PATH=$SCRATCHDIR/augustus_configs
#web discussion: http://seqanswers.com/forums/archive/index.php/t-50064.html
#augustus readme: http://augustus.gobics.de/binaries/README.TXT

export OMP_NUM_THREADS=$PBS_NUM_PPN
#AUGUSTUSCONFIGS=/software/augustus/3.3.1/src/config #or use $AUGUSTUS_CONFIG_PATH
AUGUSTUSCONFIGS=/storage/brno3-cerit/home/fussyz01/Augustus/
BUSCO_DB=eukaryota_odb9
BUSCO_HOME=/software/busco/3.0.2/src/scripts
DATADIR=/storage/brno3-cerit/home/fussyz01/rdobeli
INFILE=RETORTAMONAS_clean_renamed.fasta

#mkdir $SCRATCHDIR/augustus_configs
cp -r $AUGUSTUSCONFIGS/* $SCRATCHDIR || exit 1
cp $DATADIR/$INFILE $SCRATCHDIR || exit 3

# caution about copying $DATADIR content to $SCRATCHDIR -> use $DATADIR/* to copy content of $DATADIR than the $DATADIR itself 
export AUGUSTUS_CONFIG_PATH=$SCRATCHDIR/augustus_configs
export PATH=$PATH:/software/augustus/3.3.1/src/bin:/software/augustus/3.3.1/src/scripts

cd $SCRATCHDIR || exit 4

#augustus runs on 1 core only 
augustus --protein=on --cds=on --outfile=augustus_log_monos.txt --species=monos $INFILE
cp augustus_log_monos.txt $DATADIR
augustus --protein=on --cds=on --outfile=augustus_log_blatt.txt --species=blattamonas $INFILE
cp augustus_log_blatt.txt $DATADIR

#python $BUSCO_HOME/run_BUSCO.py -i $INFILE -o BUSCO_Retortamonas_monos-pred -l $BUSCO_DB -m genome --species monos -c 7
#python $BUSCO_HOME/run_BUSCO.py -i $INFILE -o BUSCO_Retortamonas_blatt-pred -l $BUSCO_DB -m genome --species blattamonas -c 7

# -i dataset
# -c 1-8 cores
# -m prot/tran/genome (use Augustus for genomes)
# -l busco ortholog database: busco.ezlab.org

rm -r augustus_configs
rm -r $BUSCO_DB
rm $INFILE

cp -r $SCRATCHDIR/* $DATADIR || export CLEAN_SCRATCH=false
