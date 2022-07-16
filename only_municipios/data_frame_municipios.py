from only_municipios.municipios_all import *
import pandas as pd

#########################################################################################
# INDEX TOTAL ONLY MUNICIPIOS

indice = ((len(municipios_aguascalientes_list_new)) + (len(municipios_california_list_new)) +
(len(municipios_bajacalifornia_sur_list_new)) + (len(municipios_campeche_list_new)) + 
(len(municipios_coahuila_list_new)) + (len(municipios_colima_list_new)) + 
(len(municipios_chiapas_list_new)) + (len(municipios_chiuhuahua_list_new)) + 
(len(municipios_ciudad_mexico_list_new)) + (len(municipios_durango_list_new)) + 
(len(municipios_guanajuato_list_new)) + (len(municipios_guerrero_list_new)) +
(len(municipios_hidalgo_list_new)) + (len(municipios_jalisco_list_new)) +  
(len(municipios_estado_mexico_list_new)) + (len(municipios_michoacan_list_new)) + 
(len(municipios_morelos_list_new)) + (len(municipios_nayarit_list_new)) + 
(len(municipios_nuevo_leon_list_new)) + (len(municipios_oaxaca_list_new)) + 
(len(municipios_puebla_list_new)) + (len(municipios_queretaro_list_new)) +
(len(municipios_quintana_roo_list_new)) + (len(municipios_sanluis_potosi_list_new)) + 
(len(municipios_sinaloa_list_new)) + (len(municipios_sonora_list_new)) + 
(len(municipios_tabasco_list_new)) + (len(municipios_tamaulipas_list_new)) + 
(len(municipios_tlaxcala_list_new)) + (len(municipios_veracruz_list_new)) + 
(len(municipios_yucatan_list_new)) + (len(municipios_zacatecas_list_new)) + 1)

########################################################################################
# DATAFRAME ESTRUCTURE ONLY MUNICIPIOS
df_municipios = pd.DataFrame({ 

    "Estado": estado_aguascalientes + estado_california + estado_bajacalifornia_sur +
    estado_campeche + estado_coahuila + estado_colima + estado_chiapas + estado_chiuhuahua +
    estado_ciudad_mexico + estado_durango + estado_guanajuato + estado_guerrero + 
    estado_hidalgo + estado_jalisco + estado_estado_mexico + estado_michoacan + estado_morelos + 
    estado_nayarit + estado_nuevo_leon + estado_oaxaca + estado_puebla + estado_queretaro + 
    estado_quintana_roo + estado_sanluis_potosi + estado_sinaloa + estado_sonora +
    estado_tabasco + estado_tamaulipas + estado_tlaxcala + estado_veracruz + estado_yucatan +
    estado_zacatecas,

    "Municipio": municipios_aguascalientes_list_new + municipios_california_list_new +
    municipios_bajacalifornia_sur_list_new + municipios_campeche_list_new + municipios_coahuila_list_new +
    municipios_colima_list_new + municipios_chiapas_list_new + municipios_chiuhuahua_list_new + 
    municipios_ciudad_mexico_list_new + municipios_durango_list_new + municipios_guanajuato_list_new +
    municipios_guerrero_list_new + municipios_hidalgo_list_new + municipios_jalisco_list_new + 
    municipios_estado_mexico_list_new + municipios_michoacan_list_new + municipios_morelos_list_new +
    municipios_nayarit_list_new + municipios_nuevo_leon_list_new + municipios_oaxaca_list_new +
    municipios_puebla_list_new + municipios_queretaro_list_new + municipios_quintana_roo_list_new + 
    municipios_sanluis_potosi_list_new + municipios_sinaloa_list_new + municipios_sonora_list_new + 
    municipios_tabasco_list_new + municipios_tamaulipas_list_new + municipios_tlaxcala_list_new + 
    municipios_veracruz_list_new + municipios_yucatan_list_new + municipios_zacatecas_list_new}, 
    index=list(range(1, indice)))

# REPLACING ACCENTS
df_municipios.replace(to_replace=r'á', value='a', regex=True,inplace=True)
df_municipios.replace(to_replace=r'é', value='e', regex=True,inplace=True)
df_municipios.replace(to_replace=r'í', value='i', regex=True,inplace=True)
df_municipios.replace(to_replace=r'ó', value='o', regex=True,inplace=True)
df_municipios.replace(to_replace=r'ú', value='u', regex=True,inplace=True)
df_municipios.replace(to_replace=r'ä', value='a', regex=True,inplace=True)
df_municipios.replace(to_replace=r'ë', value='e', regex=True,inplace=True)
df_municipios.replace(to_replace=r'ï', value='i', regex=True,inplace=True)
df_municipios.replace(to_replace=r'ö', value='o', regex=True,inplace=True)
df_municipios.replace(to_replace=r'ü', value='u', regex=True,inplace=True)
df_municipios.replace(to_replace=r'Á', value='A', regex=True,inplace=True)
df_municipios.replace(to_replace=r'É', value='E', regex=True,inplace=True)
df_municipios.replace(to_replace=r'Í', value='I', regex=True,inplace=True)
df_municipios.replace(to_replace=r'Ó', value='O', regex=True,inplace=True)
df_municipios.replace(to_replace=r'Ú', value='U', regex=True,inplace=True)