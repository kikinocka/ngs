#!/bin/bash

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
