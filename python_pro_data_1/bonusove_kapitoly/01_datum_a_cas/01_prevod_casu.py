# Zadani: https://kodim.cz/czechitas/python-data-1/bonusy/datum/datum/prevod-casu

from datetime import datetime

start_apolla = datetime(1969, 7, 16, 14, 32)
us_format = start_apolla.strftime("%m/%d/%Y")

print(us_format)
