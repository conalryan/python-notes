#!/usr/bin/perl
#mySorter.pl

use warnings;
use strict;
use Getopt::Long;


# declare the perl command line flags/options we want to allow
my $reverse=();
GetOptions('r|reverse' => \$reverse);

 
# quit unless we have the correct number of command-line args
my $num_args = @ARGV;
if ($num_args < 2) {
    print "\nUsage: mySorter.pl please enter at least two words\n";
    exit;
}

# my @sort = sort @ARGV;
# print "@sort \n";

# my @revSort = reverse sort @ARGV;
# print "@revSort \n";

if (!$reverse) {

	my @sorted = sort { $a cmp $b } @ARGV;
	# for numbers use my @number = sort { $a <=> $b } @unsorted;
	print "Sorter: @sorted \n";
}

if ($reverse) {

	my @revSorted = sort { $b cmp $a } @ARGV;
	print "Reverse sorted: @revSorted \n";
}