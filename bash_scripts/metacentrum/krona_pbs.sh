#!/bin/bash
#PBS -N krona
#PBS -l select=1:ncpus=10:mem=5gb:scratch_local=1gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add krona-2.8

datadir='/auto/brno3-cerit/nfs4/home/kika/oil_sands/metagenomes/P1B_1-05C_L001-ds.ec8b691bd68b44deb59919ca3da275ba/4-kraken2_assembly/'

#copy files to scratch
cp $datadir'P1B.kraken.report' $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

report='P1B.kraken.report'
out='P1B.kraken.html'


ImportTaxonomy.pl -m $PBS_NUM_PPN -t 5 $report -o $out

#copy files back
rm $report
cp -R * $datadir
