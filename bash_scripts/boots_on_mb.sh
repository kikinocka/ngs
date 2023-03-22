#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/trees/Dsl1/zw10-dsl1/combined/'

tree=$path'zw10.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.zw10.CD'
out=$path'zw10-dsl1.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
