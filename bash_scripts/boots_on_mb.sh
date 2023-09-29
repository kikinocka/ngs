#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/trees/SNAREs/combined/'

tree=$path'vps3-39.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.vps3-39.CD'
out=$path'vps3-39.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
