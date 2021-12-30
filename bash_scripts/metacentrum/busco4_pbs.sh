#!/bin/sh
#PBS -N busco4
#PBS -q default
#PBS -l select=1:ncpus=4:mem=8gb:scratch_local=10gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

#puvodne v PBS taky :os=debian9, nicmene ty uz jsou aktualizovany...
trap 'clean_scratch' TERM EXIT

module add conda-modules-py37
conda activate busco_4.0.6
#module add augustus-3.3.1
export OMP_NUM_THREADS=$PBS_NUM_PPN

#AUGUSTUSCONFIGS=/software/augustus/3.3.1/src/config #or use $AUGUSTUS_CONFIG_PATH
#export PATH=$PATH:/software/augustus/3.3.1/src/bin:/software/augustus/3.3.1/src/scripts
#AUGUSTUS_CONFIG_PATH=/storage/brno3-cerit/home/fussyz01/Augustus/augustus_configs
BUSCO_DB=eukaryota_odb10
DATADIR=/storage/brno3-cerit/home/kika/p57/predicted_proteins

cp $DATADIR/*fasta $SCRATCHDIR || exit 3
cd $SCRATCHDIR || exit 4

#augustus runs on 1 core only 
for INFILE in *fasta; do
	echo $INFILE
	#augustus --protein=on --cds=on --outfile=${INFILE/fna/gtf} --species=phaant $INFILE
	#cp ${INFILE/fna/gtf} $DATADIR
	busco -i $INFILE -o ${INFILE%.*}_eukaryota_odb10 -l $BUSCO_DB -m prot 
	#--augustus_species phaant \
	#--augustus_parameters '--protein=on --cds=on' \
	-c $OMP_NUM_THREADS
	cp -r ${INFILE%.*}_eukaryota_odb10 $DATADIR
	rm $INFILE
done

# -i dataset
# -c 1-8 cores
# -m prot/tran/genome (use Augustus for genomes)
# -l busco ortholog database: busco.ezlab.org

cp -r $SCRATCHDIR/* $DATADIR || export CLEAN_SCRATCH=false

cd $DATADIR
mkdir -p report_odb10
cp *_eukaryota_odb10/short*txt report_odb10/
cd report_odb10
for i in *txt; do mv $i ${i/_eukaryota_odb10.txt/.txt}; done
generate_plot.py --no_r -wd .
#slightly modify the R script to plot percentages not counts

#test interactively
# qsub -I -l select=1:ncpus=4:mem=8gb:scratch_local=10gb -l walltime=2:00:00
# call modules and set variables...
# for INFILE in GBNP*.fna; do busco -i $INFILE -o BUSCO_${INFILE/.fna/} -l $BUSCO_DB -m genome --augustus_species phaant -c 4 ; done
