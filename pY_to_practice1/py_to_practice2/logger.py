from datetime import datetime as dt
from time import time


def temp_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv, a') as file:
        file.write('{};temperature;{}'
                   .format(time, data))


def pres_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv, a') as file:
        file.write('{};pressure;{}'
                   .format(time, data))


def windspeed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv, a') as file:
        file.write('{};windspeed;{}'
                   .format(time, data))
