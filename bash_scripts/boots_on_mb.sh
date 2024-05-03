#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/trees/all_adaptors/ver8/combined/'

tree=$path'medium.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.medium.CD'
out=$path'medium.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
