#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/archamoebae/trees/AS/ver2/combined/'

tree=$path'as.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.as.CD'
out=$path'as.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
