#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/trees/SNAREs/'

tree=$path'MrBayes/qa.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML/RAxML_bootstrap.qa.CD'
out=$path'combined/qa.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
