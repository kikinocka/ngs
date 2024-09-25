#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/mantamonas/RABs/endocytic/ver4/'

tree=$path'MrBayes/endocytic.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML/RAxML_bootstrap.endocytic.CD'
out=$path'combined/endocytic.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
