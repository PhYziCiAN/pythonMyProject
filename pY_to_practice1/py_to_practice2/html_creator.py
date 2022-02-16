from asyncore import write
from user_interface import temp_view
from user_interface import pressure_view
from user_interface import windspeed_view

def create(device = 1):
    style = 'style = "font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '       <p {}>Temperature: {} c</p>\n'\
        .format(style, temp_view(device))
    html += '       <p {}>Windspeed: {} c</p>\n'\
        .format(style, windspeed_view(device))
    html += '       <p {}>Pressure: {} c</p>\n'\
        .format(style, pressure_view(device))
    html += '   </body>\n<html>'

    with open('index.html', 'w') as page:
        page.write(html)
    return 