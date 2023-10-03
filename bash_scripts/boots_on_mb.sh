#!/bin/bash

placer='/Users/kika/scripts/py_scripts/boots_on_mb.py'

cd '/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/trees/all_adaptors/ver6/combined/'

tree=$path'propeller-solenoid.trimal_gt-0.8.nex.con.tre'
bootstrap=$path'RAxML_bootstrap.propeller-solenoid'
out=$path'propeller-solenoid.mb+raxml.tre'

$placer $tree $bootstrap $out
