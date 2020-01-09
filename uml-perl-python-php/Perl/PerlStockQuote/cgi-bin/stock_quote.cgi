#!/usr/bin/perl

use 5.010;
use CGI;
use Finance::Quote;
use strict;
use warnings;

my $q = CGI->new();
say $q->header(), 
$q->start_html(
	-meta=>{'charset'=>'utf-8'},
	-title=>'Stock Quote',
	-author=>'Conal Ryan',
	-style=>{src=>'../css/style.css'},
);

my $safe_exchange;
my $safe_symbol;

say "<header>
		<h1>Stock Quote</h1>
	</header>
	<section>";

for my $stockExchange ($q->param('stockExchange')) {

    $safe_exchange = lc $q->escapeHTML($stockExchange);
    say "<p><strong>$safe_exchange</strong>: ";
}

for my $stockSymbol ($q->param('stockSymbol')) {

    $safe_symbol = uc $q->escapeHTML($stockSymbol);
    say "$safe_symbol </p>";
}

# create object
my $fq = Finance::Quote->new();

# retrieve stock quote
my %data = $fq->fetch($safe_exchange, $safe_symbol);
#my %data2 = $fq->fetch('nyse', 'BAC');

# print price
print "The current price of $safe_symbol on the $safe_exchange is " 
	. $data{$safe_symbol, 'price'} . "\n";
#print "The current price of BAC on the NYSE is " . $data2{'BAC', 'price'};

say "</section>";
say $q->end_html();