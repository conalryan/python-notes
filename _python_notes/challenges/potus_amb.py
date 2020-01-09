#!/usr/bin/env python

from datetime import datetime, timedelta

FILE = 'data/presidents.txt'


def get_info(term):
    dict_pres = {}
    with open(FILE) as pres_in:
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


def get_oldest():
    oldest = timedelta(0)
    pres_name = ''
    with open(FILE) as pres_in:
        for line in pres_in:
            raw_pres = line.split(':')
            dob_str = raw_pres[3].split('-')
            dob = datetime(int(dob_str[0]), int(dob_str[1]), int(dob_str[2]))
            term_str = raw_pres[8]
            if term_str != 'NONE':
                term_str = term_str.split('-')
                term = datetime(int(term_str[0]), int(term_str[1]), int(term_str[2]))
            else:
                term = datetime.now()
            age = term - dob
            if age > oldest:
                oldest = age
                pres_name = f"{raw_pres[2]} {raw_pres[1]}"

    return pres_name


def get_youngest():
    youngest = timedelta(0)
    pres_name = ''
    with open(FILE) as pres_in:
        for line in pres_in:
            raw_pres = line.split(':')
            dob_str = raw_pres[3].split('-')
            dob = datetime(int(dob_str[0]), int(dob_str[1]), int(dob_str[2]))
            term_str = raw_pres[7].split('-')
            term = datetime(int(term_str[0]), int(term_str[1]), int(term_str[2]))
            age = term - dob
            if youngest.days == 0 or age < youngest:
                youngest = age
                pres_name = f"{raw_pres[2]} {raw_pres[1]}"

    return pres_name
