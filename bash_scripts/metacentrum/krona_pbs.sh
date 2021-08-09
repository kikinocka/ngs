#!/bin/bash
#PBS -N krona
#PBS -l select=1:ncpus=15:mem=5gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add krona-2.8

datadir='/storage/brno3-cerit/home/kika/oil_sands/metagenomes/20xx0821_BML-B-first/kraken2/'

#copy files to scratch
cp $datadir'bml_meta.kraken.report' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

report='bml_meta.kraken.report'
out='bml_meta.kraken.html'


ImportTaxonomy.pl -m $PBS_NUM_PPN -t 5 $report -o $out

#copy files back
rm $report
cp -R * $datadir
