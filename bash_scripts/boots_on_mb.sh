#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/archamoebae/trees/AAT/ver7/combined'

tree=$path'aat.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.aat.CD'
out=$path'aat.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
