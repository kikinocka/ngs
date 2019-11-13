#!/bin/sh
#PBS -N qualiMap
#PBS -q default
#PBS -l select=1:ncpus=15:mem=1gb:scratch_local=10gb:os=debian9
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module ad qualiMap-11_12-16

mapping='/storage/brno3-cerit/home/kika/sags/reassembly/mapping_bwa/'
outdir='/storage/brno3-cerit/home/kika/sags/reassembly/reports/qualimap_bwa/'

#copy files to scratch
cp $mapping'EU1718_bwa_mapped_all.sorted.bam' $SCRATCHDIR

bam='EU1718_bwa_mapped_all.sorted.bam'


#compute on scratch
cd $SCRATCHDIR
qualimap bamqc -nt $PBS_NUM_PPN -bam $bam -outdir $SCRATCHDIR -outformat pdf

#copy files back
rm $bam
cp -r * $outdir
