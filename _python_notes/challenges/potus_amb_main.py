#!/usr/bin/env python

import potus_amb

pres = potus_amb.get_info(1)
print(pres)


oldest = potus_amb.get_oldest()
print(oldest)

youngest = potus_amb.get_youngest()
print(youngest)
