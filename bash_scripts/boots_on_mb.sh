#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/trees/DSL1/rint1-tip20/combined_Lael/'

tree=$path'rint1.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.rint1.CD'
out=$path'rint1.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
