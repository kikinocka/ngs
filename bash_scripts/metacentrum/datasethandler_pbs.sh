#/bin/bash
#PBS -N datasethandler
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=2gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

# add modules
module add python36-modules-gcc
module add iqtree-1.6.8
module add mafft-7.313
module add trimal-1.4

#copy files to scratch
DATADIR='/storage/brno3-cerit/home/kika/proteromonas/SOD_tree/ver3'

cp '/storage/brno2/home/kika/scripts/kika/py_scripts/datasethandler-server.py' $SCRATCHDIR
cp $DATADIR'/'*.fa $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
python datasethandler-server.py \
	-i batch \
	-a mafft \
	--trimalparams='-gt 0.5' \
	-t iqtree \
	-b \
	--maxcores $PBS_NUM_PPN

#'-d', '--directory', help='Change working directory', default='.'
#'-i', '--infile', help='Fasta/Phylip set to be analyzed', default="batch"
#'--maxcores', help='Maximum cores to use for multithreading', default=20
#'-a', '--aligner', help='Aligner', default='mafft'
#'-t', '--treemaker', help='Program for tree inference', default='iqtree'
#'-n', '--no_dedupe', help='Do not filter duplicates', action='store_true'
#'--alignerparams', help='Custom aligner parameters, check with manual', default=''
#'--trimalparams', help='Custom TrimAl parameters, check with manual', default=''
#'-b', '--ufbootstrap', help='Ultra-fast boostrap calculation', action='store_true'
#'-B', '--bootstrap', help='Boostrap calculation', action='store_true'
#'--shalrt', help='Calculate SH-aLRT', action='store_true'
#'-g', '--no_guide', help='Do not perform guide tree inference', action='store_true'
#'--treeparams', help='Custom tree inference parameters, check with manual', default=''
#'-s', '--mark_similarity', help='Mark similarity on branches', action='store_true'

#copy files back
cp -R RESULT $DATADIR
cp -R temp $DATADIR
cp error.log $DATADIR
