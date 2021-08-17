#!/bin/bash
#PBS -N krona
#PBS -l select=1:ncpus=10:mem=5gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add krona-2.8

datadir='/auto/brno3-cerit/nfs4/home/kika/oil_sands/metagenomes/P3B_1-06D_L001-ds.435324be81dc4260a8e3e8dbb5ed960c/4-kraken2_assembly/'

#copy files to scratch
cp $datadir'P3B.kraken.report' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

report='P3B.kraken.report'
out='P3B.kraken.html'


ImportTaxonomy.pl -m $PBS_NUM_PPN -t 5 $report -o $out

#copy files back
rm $report
cp -R * $datadir
