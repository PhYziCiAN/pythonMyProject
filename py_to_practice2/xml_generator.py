from user_interface import temp_view
from user_interface import pressure_view
from user_interface import windspeed_view

def create(device=1):
    xml = '<xml>\n'
    xml += '    <temperature units = "c">{}</temperature>\n'\
        .format(temp_view(device))
    xml += '    <pressure units = "mmHg">{}</pressure>\n'\
        .format(pressure_view(device))
    xml += '    <windspeed units = "m/s">{}</windspeed>\n'\
        .format(windspeed_view(device))
    with open('data.xml','w') as page:
        page.write(xml)
    return xml

def create1(data, device=1):
    t, p, w = data
    xml = '<xml>\n'
    xml += '    <temperature units = "c">{}</temperature>\n'\
        .format(t)
    xml += '    <pressure units = "mmHg">{}</pressure>\n'\
        .format(p)
    xml += '    <windspeed units = "m/s">{}</windspeed>\n'\
        .format(w)
    with open('new_data.xml','w') as page:
        page.write(xml)
    return data