#!/bin/bash

#1) short = sys.argv[1] 
# short name of the taxon i.e. Homosapi for Homo sapiens, Convention is 4 characters for GENUS and 4 for SPECIES
#2) long = sys.argv[2] 
# long name of the taxon i.e. "Homo_sapiensNCBI-RefSeqCDS" !!!!! Note that you must have an "_" and it can only have 1 "_" !!! i.e. if you do not know the species name do this: Homo_spXXXXXXXXX--- I like to put where the Data came from after the species name
#3) code = sys.argv[3] 
# genetic code usually "1"
#4) mode = sys.argv[4] 
# "AA" or "NUC" : either 'AA' for a protein dataset in amino acids or 'NUC' for a nucleotide dataset (i.e., EST or CDS)##
#5) refdat = sys.argv[5] 
# reference genes that you want to search for --- here it is 
#6) dbpath = sys.argv[6] 
# place where your short.fas is usually "./"
#7) next = sys.argv[7] 
# shortname of your next taxon to add i.e "Arabthal" or if you are done adding taxa for the day just put END.4-26-2013 (todays date)
#8) runBMGE = sys.argv[8] 
# Do you want to run BMGE? OPTIONS: "yes", "no", or "yesMB"? -- don't do until the end of adding -- yesMB will make submissions for SGT on Scinet (Currently For Matt Brown Only, makes a set of shell scripts for running on SCINET)


datadir='/home/users/kika/bordor/'
script=$datadir'AddPipeline3.1.py'
dbpath=$datadir
refdat=$datadir'Bordor.351.refdat.txt'
short='EU17'
long='Euglenozoa_EU17-JerSAGs'
next='EU18'
code=1
mode=NUC
runBMGE=no

cd $datadir
python2 $script $short $long $code $mode $refdat $dbpath $next $runBMGE
