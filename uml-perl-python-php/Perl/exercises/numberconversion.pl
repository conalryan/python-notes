#!/usr/bin/perl
#numberconversions.pl

# 0 for octal 			from 0 to 7		oct()
# 0b for binary			from 0 to 1
# 0x for hexadecimal	from 0 to F 	hex()

use warnings;
use strict;

print "Number conversions \n\n Please enter a hexadecimal number: ";

my $hexNum = <STDIN>;
my $decNum= hex($hexNum);

print "The hexadecimal number $hexNum is the decimal number $decNum";

print "Please enter an octal number: ";

my $octNum = <STDIN>;
my $decNum2= oct($octNum);

print "The oct number $octNum is the decimal number $decNum2";