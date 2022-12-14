#!/bin/bash
#PBS -d .
#PBS -v PATH
#PBS -N repeatmodeler
#PBS -l nodes=1:ppn=10
#PBS -l walltime=24:00:00

bash /home/users/kika/dfam-tetools.sh

cd '/home/users/kika/blastocrithidia/final_assemblies/'
genome='Bfru_genome_final.fa'
name=${genome%_final.fa}

#Generate the RepeatModeler sequence database
BuildDatabase -name $name $genome

#Run RepeatModeler
RepeatModeler -database $name -threads 10 -LTRStruct

# #How many consensus sequences have been predicted?
# grep -c '>' $name'-families.fa' > 
# #How is the distribution of repeats by types?
# grep '>' $name'-families.fa' | sed -r 's/.+#//' | sed -r 's/\s+.+//' | sort | uniq -c > 

python3 /home/users/kika/scripts/py_scripts/slackbot.py OSU: RepeatModeler done
