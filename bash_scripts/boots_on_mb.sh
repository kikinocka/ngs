#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/archamoebae/trees/AK/ver7/combined'

tree=$path'ak.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.ak.CD'
out=$path'ak.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
