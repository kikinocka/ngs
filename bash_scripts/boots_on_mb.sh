#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/archamoebae/trees/transporters/ver3/combined'

tree=$path'transporters.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.transporters.CD'
out=$path'transporters.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
