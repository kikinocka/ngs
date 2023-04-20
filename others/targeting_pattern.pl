#!/usr/bin/env perl
#JPS 31 aout 1999
#JPS modifie pour Fred 16 juin 2003

format = 
@<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< @>>>>>>>> @<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
$db_desc,$position,$read_pattern
.
format MAIL =
@<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< @>>>>>>>> @<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
$db_desc,$position,$read_pattern
.

$|=1; 


$db = $ARGV[0];
$file = $ARGV[1];

# open du fichier avec les sequences FASTA contenant les pattern
open (OUT, ">$file.$$") or die "Can't open result file $file.$$: $!\n" ;
# scan du fichier TMP contenant les pattern soumis
open (TMP , "$file") or die "Can't open pattern file $file: $!\n" ;
while (<TMP>)	{
#	if ( /^>\s*(\S+)\s*(.*?)\s*$/) {
	if ( /^>\s*(\S+)\s*(.*)$/) {
		$new_pat_desc = $1;
		$new_desc = $2;
		if ( $pattern ne "")	{
    			&db_scan;   # $pat_desc et $pattern sont utilisables
			}
		$pat_desc = $new_pat_desc;
		$desc = $new_desc;
		$pattern = "";
		} 
	else {
		s/(\S*)\s*/$1/;
		$pattern .= $_ ;
	}
	if ( eof )  {
		if ($pattern ne "")	{
			&db_scan;
			}
		}
}
close TMP;

#if (!$debug)	{
#unlink "/tmp/pattern.$$";

#}
exit;

#---
sub db_scan	{
  print "================================================================================\n";
  print "$pat_desc      $pattern\n";
  print "--------------------------------------------------------------------------------\n";
  if (eval { "" =~ /$pattern/; 1}) {
    $hit_count = 0;
    open (DB, "$db") or die "Can't open db file $db: $!\n";
    while (<DB>) {
  	#if ( /^>\s*(\S+\s\S+)\s*(.*?)\s*$/) {
  	if ( /^>\s*(\S+)\s*(.*?)\s*$/) {
  	    $new_db_desc = $1;
	    $new_db_comment = $2;
  	    if ($db_seq ne "")	{
		  	&match;
		  	}
		$db_desc = $new_db_desc;
		$db_comment = $new_db_comment;
		$db_seq = "";
		}
	else	{
		s/(\S*)\s*/$1/;
		$db_seq .= $_;
	}
	if (eof)	{
		if ($db_seq ne "")	{
			&match;
			}
		}
	}
	close DB;
    if ($hit_count == 0)	{
  	print "No hit found\n";
  	}
  } else {
  print "$pattern  is not a valid pattern\n\n";
  }
}
	
#---
sub match	{
	while ($db_seq =~ /($pattern)/gi)  {
  		$read_pattern= $1;
#		unless  ( $read_pattern =~ /\*/) {
  			$position = index ($db_seq, $read_pattern);
  			write ;
  			print OUT ">$db_desc $db_comment\n";
  			print OUT "$db_seq\n";
  			$hit_count++;
  			$hit{$db_desc} = $hit{$db_desc}." ".$pat_desc; 
			$comment{$db_desc} = $db_comment;
#			}
  		}
}

