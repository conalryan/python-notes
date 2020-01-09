#!usr/bin/perl
use warnings;
use strict;

###############################################################################
# variables
# scalar variables use $
$myInteger = 3;	#integer
$myFloat = 22.55; #float
$myString = "Here is my string"; #string

# arrays start with @
@myArray = ("Lisa", "Conal", "Liam"); #array
@myMixedArray = ("String", 45, 99.18);

print "$myArray[0] \n";
print "$myArray[1] \n";
print "$myArray[2] \n";

# print concat
print "Some stuff to print " . $myMixedArray[1] . "\n";

print <<EOF;
This is
a multiline
string
EOF

# escape sequences
# ' " \ @ ( ) { } [ ] $ % 

###############################################################################
# COMPARITIVE OPERATORS
# if else elseif regular expressions

# Get input from user
$userInput = <STDIN>;
chomp $userInput; #is this correct syntax?

# CONDITIONAL OPERATORS
# < > == != lt gt eg ne 

# COMPARISON OPERATORS
# && || 

# REGULAR EXPRESSION
# =~ /bunny/gi
if ($userInput =~ /bunny/gi) {
	# TODO
}  

# g means global i.e. look at the entire string. w/out g it would only replace 
# the first occurrences.
# i means case-insensitive

sleep(1); # pause program

# search and replace =~ s/searchThis/replaceThat/gi;
$animal =~ s/cat/rabbit/gi;

# strip out spaces
$quote =~ s/\s//g;

# find
$cat =~ m/cat/

# command line search and replace
perl -pi -e 's/Shannon Morse/Shannon McTillidor/g' *.txt
perl -pi -e 's/\.html/\.php/g' *.html #replace all .html with .php
perl -pi -e 's/\<\!--[^\>]+-->//g' *.html #remove comments from html
perl -pi -e 's/(Shan\S+) McTillidor/Sailor $1/g' *.txt #Change Shan... McTillidor to Sailor Shan...

# -e Provides program as an argument rather than in a file
# -i Modifies the input file in-place
# -p Runs the file with:
while (<>) {
	# execute your command line code here
}
continue {
	print or die "-p destination: $!\n";
}

###############################################################################
# DYNAMIC WEBPAGE
#!usr/bin/perl

# set content type for the page
print "Content-type: text/html\n\n";

# start html
print "<html><body>\n";

print "<ul>";
for($count = 0; $count <10; $count++) {
	print "<li>$count</li>";
}
print "</ul>"

print "</body></html>"

###############################################################################
