#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/trees/SM/ver4/combined/'

tree=$path'sm.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.sm.CD'
out=$path'sm.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
