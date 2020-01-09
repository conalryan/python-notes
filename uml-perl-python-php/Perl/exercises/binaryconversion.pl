#!/usr/bin/perl
#binaryconversion.pl

use warnings;
use strict;

print "Enter a number to convert: ";

chomp(my $decimal = <STDIN>);

print "\nConverting $decimal to binary...\n";

my @array;

my $num;

while($decimal >= 1)
{

if($decimal == 1) {

    $num .= 1;

    last;
}

my $remainder = $decimal%2;

$num .= $remainder;

$decimal = $decimal/2;


}

print $num."\n";