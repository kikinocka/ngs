#!/bin/bash
##This is an example script PhyloBayes.sh
##These commands set up the Grid Environment for your job:
#PBS -N APM_PB
#PBS -l nodes=1,walltime=5000:00:00
#Print the Host name of Node
echo "Hostname is " $HOSTNAME
##print the time and date
##Print  working directory
pwd
##Print Date
date
##send PhyloBayes command to Cluster nodes
pb -d APM_phylogenetics_ML -nchain 4 100 0.1 100 -lg APM_phylogenetics_ML_out
##End Script


#PBS –N  DesiredJobName
#pb –d filename.phy –nchain 4 100 0.1 100 –lg nameofoutput
	#d is the inputfile
	#Nchain 4 means 4 chains run
	#100 means that 500 cycles will run (100x5, 5, is the default burnin factor (20% because 1/5=0.20; You can change it to 25% if you want but this is default)
	#0.1 cutoff means that cutoff for discrepancies between two chains and effective sample sizes is 0.1 and run will stop if this dips below 0.1. Check PB documentation for further explanation. 
	#Second 100 stands for effective sample sizes are greater than 100 
	#-lg = model; can change this to something different such as mixture model CAT-GTR (Here is a paper describing why this mixture model is good for Bayesian analysis if you are interested - https://academic.oup.com/mbe/article/21/6/1095/1050747)
