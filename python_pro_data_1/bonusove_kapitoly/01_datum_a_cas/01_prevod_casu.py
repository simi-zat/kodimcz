# Zadani: https://kodim.cz/czechitas/python-data-1/bonusy/datum/datum/prevod-casu

from datetime import datetime

start_Apolla = datetime(1969, 7, 16, 14, 32)
us_format = start_Apolla.strftime("%m/%d/%Y")

print(us_format)
