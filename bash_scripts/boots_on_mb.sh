#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/trees/retromer-retriever/vps26-DSCR3/ver3/combined/'

tree=$path'vps26.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.vps26.CD'
out=$path'vps26.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
