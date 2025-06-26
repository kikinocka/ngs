#!/bin/bash

server='amoebae'
scp_dir='/home/kikaz/amoebae_jpp/resources/local_db_files'
data_dir='/Users/kika/data/eukprot_v3/'

scp $data_dir'EP00114_'* $server:$scp_dir
scp $data_dir'EP00118_'* $server:$scp_dir
scp $data_dir'EP00119_'* $server:$scp_dir
scp $data_dir'EP00059_'* $server:$scp_dir
scp $data_dir'EP00067_'* $server:$scp_dir
scp $data_dir'EP00074_'* $server:$scp_dir
scp $data_dir'EP00076_'* $server:$scp_dir
scp $data_dir'EP00040_'* $server:$scp_dir
scp $data_dir'EP00042_'* $server:$scp_dir
scp $data_dir'EP00044_'* $server:$scp_dir
