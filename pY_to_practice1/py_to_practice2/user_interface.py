import data_provider as provider
import logger as log
def temp_view(sensor):
    data = provider.get_temperature(sensor)
    log.temp_logger(data)
    return data

def pressure_view(sensor):
    data = provider.get_pressure(sensor)
    log.pres_logger(data)
    return data

def windspeed_view(sensor):
    data = provider.get_windspeed(sensor)
    log.windspeed_logger(data)
    return data
