# Zadani: https://kodim.cz/czechitas/python-data-1/bonusy/datum/datum/doprava-vecere

from datetime import datetime, timedelta

order_placed = datetime(2020, 11, 13, 19, 47)

accept_time = timedelta(minutes=8, seconds=35)
cooking_time = timedelta(minutes=30)
transfer_time = timedelta(minutes=25, seconds=30)

expected_delivery = order_placed + accept_time + cooking_time + transfer_time
print(f"Expected delivery time is: {expected_delivery.strftime('%H:%M:%S')}")
