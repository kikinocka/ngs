
###
FNR == 1 { 
count = 1

gsub(/evm\.[a-zA-Z]+\.scaffold[0-9]+_[0-9]+\.[0-9]+/,"Pelo"count)

print # print the line after replace
}
FNR > 1 { 
	if ($1 == "###"){ # it is a new gene so moving on
	count++
	print $0
	}
	else{ # still the same gene
		gsub(/evm\.[a-zA-Z]+\.scaffold[0-9]+_[0-9]+\.[0-9]+/,"Pelo"count)
		print
	}
}

