from random import randint

def get_temperature(sensor):
    return randint(0,183) if sensor else randint(0,20)

def get_pressure(sensor):
    if sensor:
        return randint(720,750)
    else:
        return randint(750,770)

def get_windspeed(sensor):
    if sensor == 1:
        return randint(1,30)
    else:
        return 0