#!/usr/bin/perl

#currencyconverter.plx

use warnings;

use strict;

print "Currency converter\n\nPlease enter the exchange rate: ";

my $xRate = <STDIN>;

print "Please enter the amount: ";

my $amt = <STDIN>;

print "$amt is ", ($amt/$xRate), "\n";