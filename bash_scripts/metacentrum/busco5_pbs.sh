#!/bin/sh
#PBS -N busco5
#PBS -q default
#PBS -l select=1:ncpus=5:mem=8gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add conda-modules-py37
conda activate busco

# #available datasets
# busco --list-datasets

assembly_dir='/storage/brno3-cerit/home/kika/archamoebae/prot_assemblies_filtration-20220127'

#copy files to scratch
cp $assembly_dir'/'*.faa $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

mode='prot'
lineage='eukaryota_odb10'

mkdir BUSCO_summaries_$lineage

for fasta in *.faa; do
	echo $fasta
	base=${fasta}_$lineage
	busco -i $fasta -l $lineage -o $base -m $mode -c $PBS_NUM_PPN
	
	cp $base'/short_summary.specific.'$lineage'.'$base'.txt' BUSCO_summaries_$lineage
done

generate_plot.py -wd BUSCO_summaries_$lineage


#copy files back
rm *.faa
cp -r * $assembly_dir
