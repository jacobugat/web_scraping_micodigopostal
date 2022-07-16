from only_municipios.municipios_all import *
from bs4 import BeautifulSoup
import requests

def getting_variables(aa):
    url_link = aa
    page_link = requests.get(url_link)
    soup_document = BeautifulSoup(page_link.text, "html.parser")
    municipios = soup_document.find("table", class_ = "tabla-general")
    municipio_list = list()
    for i in municipios.find_all("tbody"):
        rows = i.find_all("tr")
        for row in rows:
            municipio_list.append(row.find_all("td")[0].text.strip())
            
    municipio_list_new = []
    for i in municipio_list:
        if(i !=""):
            municipio_list_new.append(i)
    print("scraping: " + aa)
    return municipio_list_new

def estados(list_new, state):
    estado = list()
    for a in list_new:
        estado.append(state)        
    return estado




