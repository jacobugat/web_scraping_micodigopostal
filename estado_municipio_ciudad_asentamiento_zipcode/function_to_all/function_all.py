from estado_municipio_ciudad_asentamiento_zipcode.all_links import *
import pandas as pd

def create_all(link, state):
    url_municipio = (link)
    dfs = pd.read_html(url_municipio)                                                                                                        
    df = dfs[0]                                                                                                          
    new_df = df.assign(Estado= state)
    df3 = new_df[['Estado', 'Municipio', 'Ciudad', 'Asentamiento▼','Código Postal']]
    eliminar = df3[df3["Municipio"]== "(adsbygoogle = window.adsbygoogle || []).push({});"].index
    dataframe_clear = df3.drop(eliminar)
    dataframe_clear.rename(columns={'Asentamiento▼': 'Asentamiento'}, inplace=True)
    dataframe_clear.rename(columns={'Código Postal': 'Codigo Postal'}, inplace=True)
    print ("scraping: " + link)
    return dataframe_clear