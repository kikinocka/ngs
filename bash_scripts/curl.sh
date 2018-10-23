#login 
curl -d "u=user&p=password" --cookie-jar cjar http://mokosz.natur.biocev.org/doku.php?do=login

#downloading
curl --cookie cjar --cookie-jar cjar -o pelo6_r2.fastq.gz http://mokosz.natur.biocev.org/lib/exe/fetch.php?media=pelomyxa:pelo6_s5_l001_r2_001_tr.fastq.gz

