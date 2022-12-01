#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/archamoebae/trees/Rho/ver7_muscle/combined/'

tree=$path'miro.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.miro.CD'
out=$path'miro.CD.trimal_gt-0.8.nex.mb+raxml.tre'

$placer $tree $bootstrap $out
