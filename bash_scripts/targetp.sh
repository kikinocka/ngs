#!/bin/bash

targetp='/home/kika/programs/targetp-1.1/targetp'
workdir='/home/kika/ownCloud/pelomyxa_schiedti/mito_proteins/fes_cluster_assembly/cia/'
infile=$workdir'additional'
outfile=$workdir'additional_targetp.txt'
plant='P'
non_plant='N'

$targetp -$non_plant -c $infile > $outfile
