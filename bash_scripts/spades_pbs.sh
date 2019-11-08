#!/bin/bash
#PBS -N SPAdes
#PBS -q uv@wagap-pro.cerit-sc.cz -l select=1:ncpus=20:ompthreads=20:mem=100gb:scratch_local=100gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add modules
module add spades-3.11.1bin

reads='/storage/brno3-cerit/home/kika/sags/reassembly/trimmed_reads/'
outdir='/storage/brno3-cerit/home/kika/sags/reassembly/spades/'

#copy reads to scratch
cp $reads'EU17_trimmed_merged.fq.gz' $reads'EU17_r1_trimmed_unmerged.fq.gz' $reads'EU17_r2_trimmed_unmerged.fq.gz' $reads'EU17_all_unpaired.fq.gz' $SCRATCHDIR
cp $reads'EU18_trimmed_merged.fq.gz' $reads'EU18_r1_trimmed_unmerged.fq.gz' $reads'EU18_r2_trimmed_unmerged.fq.gz' $reads'EU18_all_unpaired.fq.gz' $SCRATCHDIR

pe1m='EU17_trimmed_merged.fq.gz'
pe11='EU17_r1_trimmed_unmerged.fq.gz'
pe12='EU17_r2_trimmed_unmerged.fq.gz'
pe1u='EU17_all_unpaired.fq.gz'

pe2m='EU18_trimmed_merged.fq.gz'
pe21='EU18_r1_trimmed_unmerged.fq.gz'
pe22='EU18_r2_trimmed_unmerged.fq.gz'
pe2u='EU18_all_unpaired.fq.gz'

report='spades_report.txt'

#compute on scratch
cd $SCRATCHDIR
spades.py --sc --careful -t $PBS_NUM_PPN
--pe1-m $pe1m --pe1-1 $pe11 --pe1-2 $pe12 --pe1-s $pe1u \
--pe2-m $pe2m --pe2-1 $pe21 --pe2-2 $pe22 --pe2-s $pe2u \
-o out 2> $report

#copy results to your folder
rm $pe1m $pe11 $pe12 $pe1u $pe2m $pe21 $pe22 $pe2u
cp -r * $outdir
