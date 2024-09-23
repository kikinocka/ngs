#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/mantamonas/RABs/ver3/'

tree=$path'MrBayes/rabs.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML/RAxML_bootstrap.rabs.CD'
out=$path'combined/rabs.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
