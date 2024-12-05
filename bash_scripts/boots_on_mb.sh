#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_ESCRTs/ESCRT-0/tree/backbone/ver10/'

tree=$path'mrbayes/amorphea.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'iqtree_bs/amorphea.CD.trimal_gt-0.8.aln.boottrees'
out=$path'combined/amorphea.CD.mb+iq.tre'

$placer $tree $bootstrap $out
