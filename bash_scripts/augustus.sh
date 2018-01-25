#!/bin/sh

cd /home/kika/blastocrithidia/augustus
#augustus --species=blastocrithidia Blastocrithidia_for_Augustus.gb.test | tee firsttest.out
optimize_augustus.pl --species=blastocrithidia /home/kika/blastocrithidia/augustus/Blastocrithidia_for_Augustus.gb.train --AUGUSTUS_CONFIG_PATH=/home/kika/bin/augustus-3.2.3/config