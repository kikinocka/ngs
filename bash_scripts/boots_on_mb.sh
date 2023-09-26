#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/archamoebae/trees/acs/ver5/combined/'

tree=$path'acs.CD.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.acs.CD'
out=$path'acs.CD.mb+raxml.tre'

$placer $tree $bootstrap $out
