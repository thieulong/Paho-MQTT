import random
import time

def generate_data(device_id):
    random_methane = round(random.uniform(5,95),2)
    methane_gas = random_methane
    random_air = round(random.uniform(5,95),2) 
    air_pressure = random_air
    trend = random.randint(0,1)
    if trend == 0:
        methane_gas = random_methane - round(random.uniform(0,5),2)
        air_pressure = random_air - round(random.uniform(0,5),2)
    elif trend == 1:
        methane_gas = random_methane + round(random.uniform(0,5),2)
        air_pressure = random_air + round(random.uniform(0,5),2)
    
    methane_gas = round(methane_gas, 2)
    air_pressure = round(air_pressure, 2)
    
    return '{},{},{}'.format(device_id, methane_gas, air_pressure)