#!/bin/bash
#PBS -N krona
#PBS -l select=1:ncpus=10:mem=5gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add krona-2.8

datadir='/auto/brno3-cerit/nfs4/home/kika/oil_sands/metagenomes/P2S_1-01A_L001-ds.9f42a90caf694c0ab5686f0e22e79319/4-kraken2_assembly/'

#copy files to scratch
cp $datadir'P2S.kraken.report' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

report='P2S.kraken.report'
out='P2S.kraken.html'


ImportTaxonomy.pl -m $PBS_NUM_PPN -t 5 $report -o $out

#copy files back
rm $report
cp -R * $datadir
