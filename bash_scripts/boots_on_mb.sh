#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/trees/ARFs/ph-arf/ver4/'

tree=$path'MrBayes/arfs_reduced.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML/RAxML_bootstrap.arfs_reduced.CD'
out=$path'combined/arfs_reduced.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
