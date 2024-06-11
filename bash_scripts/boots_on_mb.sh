#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/trees/ARFs/ph-arf/ver3/combined/'

tree=$path'arfs_reduced.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'arfs_reduced.CD.trimal_gt-0.8.aln.ufboot'
out=$path'arfs_reduced.CD.mb+iqt.tre'

$placer $tree $bootstrap $out
