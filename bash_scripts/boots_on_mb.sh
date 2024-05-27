#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/trees/ARFs/ph-arf/ver2/combined/'

tree=$path'RAxML_bootstrap.arfs_reduced.CD.tre'
bootstrap=$path'arfs_reduced.CD.trimal_gt-0.8.aln.ufboot'
out=$path'arfs_reduced.CD.raxml+iqtree.tre'

$placer $tree $bootstrap $out
