#!/usr/bin/env python


def get_info(term):
    dict_pres = {}
    with open('data/presidents.txt') as pres_in:
        for line in pres_in:
            raw_pres = line.split(':')
            if raw_pres[0] == str(term):
                dict_pres = {
                    'term': raw_pres[0],
                    'last_name': raw_pres[1],
                    'first_name': raw_pres[2],
                    'dob': raw_pres[3],
                    'dod': raw_pres[4],
                    'city': raw_pres[5],
                    'state': raw_pres[6],
                    'term_start': raw_pres[7],
                    'term_end': raw_pres[8],
                    'party': raw_pres[9]
                }
    return dict_pres
