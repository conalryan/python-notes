#!/usr/bin/env python

"""
SQL Injection
    "Hijacks" SQL code
    Result of string formatting
    Always use parameterized statments
    Attacker embeds SQL commands in input data
"""
good_input = 'Google'
# Input would come form a web form, for instance
malicious_input  = "'; drop table customers; -- "

naive_format = "select * from customers where company_name = '{}' and company_id != 0"

# String formatting naively adds the user input to a field, expecting only a customer name
good_query = naive_format.format(good_input)
# String formatting naively adds the user input to a field, expecting only a customer name
malicious_query = naive_format.format(malicious_input)

print("Good query:")
# Non-malicious input works fine
print(good_query)
print()

print("Bad query:")
# Query now drops a table ('--' is SQL comment)
print(malicious_query)



