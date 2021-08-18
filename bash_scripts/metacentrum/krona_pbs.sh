#!/bin/bash
#PBS -N krona
#PBS -l select=1:ncpus=10:mem=5gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add krona-2.8

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/P3S_1-02B_L001-ds.971c07c67a83443891de04bf749cee0b/4b-kraken2-microbial_reads/'

#copy files to scratch
cp $datadir'P3S.kraken.report' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

report='P3S.kraken.report'
out='P3S.kraken.html'


ImportTaxonomy.pl -m $PBS_NUM_PPN -t 5 $report -o $out

#copy files back
rm $report
cp -R * $datadir
