#!/bin/bash

server='amoebae'
scp_dir='/home/kikaz/amoebae_jpp/resources/local_db_files'
data_dir='/Users/kika/data/eukprot_v3/'

scp $data_dir'EP00290_'*.fasta $server:$scp_dir
scp $data_dir'EP00291_'*.fasta $server:$scp_dir
scp $data_dir'EP00294_'*.fasta $server:$scp_dir
scp $data_dir'EP00295_'*.fasta $server:$scp_dir
scp $data_dir'EP00656_'*.fasta $server:$scp_dir
scp $data_dir'EP00658_'*.fasta $server:$scp_dir
scp $data_dir'EP00164_'*.fasta $server:$scp_dir
scp $data_dir'EP00302_'*.fasta $server:$scp_dir
scp $data_dir'EP00314_'*.fasta $server:$scp_dir
scp $data_dir'EP00315_'*.fasta $server:$scp_dir
scp $data_dir'EP00320_'*.fasta $server:$scp_dir
scp $data_dir'EP00323_'*.fasta $server:$scp_dir
scp $data_dir'EP00327_'*.fasta $server:$scp_dir
