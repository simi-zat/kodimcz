# Zadani: https://kodim.cz/czechitas/python-data-1/bonusy/datum/datum/cas-od-startu

from datetime import datetime

launched = datetime(2020, 2, 10, 5, 3)
launch_day = launched.weekday()

print(f"Solar Orbiter launched on {launched} that was {launched.strftime('%A')}")

current_time = datetime.now()

print(f"Time from the launch: {current_time - launched}")
