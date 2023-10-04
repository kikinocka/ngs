#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/trees/RABs/rabs2-4-14/ver2/combined/'

tree=$path'rabs2-4-14.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.rabs2-4-14.CD'
out=$path'rabs2-4-14.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
