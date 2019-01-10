from django.conf import settings
import requests

def get_dolares_entre_fechas(year, month, day, year2, month2, day2):
    url = "https://api.sbif.cl/api-sbifv3/recursos_api/dolar/periodo/{}/{}/dias_i/{}/{}/{}/dias_f/{}" .format(year, month, day, year2, month2, day2)
    params = {'apikey': settings.API_KEY_SBIF, 'formato': 'json'}
    response = requests.get(url, params=params)
    dolar = response.json()
    if response.status_code == 200:
        dolares_list = {'valores': dolar['Dolares']}
        return dolares_list
    else:
        return response


def get_uf_entre_fechas(year, month, day, year2, month2, day2):
    url = "https://api.sbif.cl/api-sbifv3/recursos_api/uf/periodo/{}/{}/dias_i/{}/{}/{}/dias_f/{}" .format(year, month, day, year2, month2, day2)
    params = {'apikey': settings.API_KEY_SBIF, 'formato': 'json'}
    response = requests.get(url, params=params)
    uf = response.json()
    if response.status_code == 200:
        uf_list = {'valores': uf['UFs']}
        return uf_list
    else:
        return response

def get_tmc_entre_fechas(year, month, year2, month2):
    url = "https://api.sbif.cl/api-sbifv3/recursos_api/tmc/periodo/{}/{}/{}/{}" .format(year, month, year2, month2)
    params = {'apikey': settings.API_KEY_SBIF, 'formato': 'json'}
    response = requests.get(url, params=params)
    tmc = response.json()
    if response.status_code == 200:
        tmc_list = {'valores': tmc['TMCs']}
        return tmc_list
    else:
        return response

def getTiposTmc(tmc):
    list_tipos = []
    for num, tasa in enumerate(tmc['valores']):
        list_tipos.append(tasa['Tipo'])
    list_tipos = list(set(list_tipos))
    list_tipos.sort()
    return list_tipos

def getDatesTmc(tmc):
    list_dates = []
    for num, tasa in enumerate(tmc['valores']):
        list_dates.append(tasa['Fecha'])
    list_dates = list(set(list_dates))
    list_dates.sort()
    return list_dates

