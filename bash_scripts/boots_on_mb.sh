#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/archamoebae/trees/GCS-L/ver8/combined'

tree=$path'gcsL.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.gcsL.CD'
out=$path'gcsL.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
