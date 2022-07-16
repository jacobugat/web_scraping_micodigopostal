from only_municipios.data_frame_municipios import *
from only_municipios.municipios_all import *
from estado_municipio_ciudad_asentamiento_zipcode.all_links.all_links import *
from estado_municipio_ciudad_asentamiento_zipcode.all_links.all_links_second import *
from estado_municipio_ciudad_asentamiento_zipcode.data_frame_all.dataframe_all import *
from datetime import datetime

###########################################################################################
# CHECKING NEW MUNICIPIOS

df_municipios_compare = df_municipios
new_result_2 = new_result
new_result_compare = new_result.drop(["Ciudad", "Asentamiento", "Codigo Postal"], axis=1)
new_result_compare_new = new_result_compare.drop_duplicates()
final_compare_municipios = df_municipios_compare.merge(new_result_compare_new, how='outer', indicator='union')
compare_municipios = final_compare_municipios[final_compare_municipios.union=='left_only']

if (compare_municipios.empty):
    print ("Theres is not any new municipios to add at the program")
    enter = input("Enter to continue and print the document micodigopostal in excel: ")

    ##########################################################################################
    # ALL INFORMATION, ESTADO, MUNICIPIO, CIUDAD, ASENTAMIENTO, ZIP CODE
    date_result = (datetime.today().strftime('%d_%m_%Y'))
    new_results.to_excel("micodigopostal_" + date_result +  ".xlsx", index=False)

    #########################################################################################
    # FILE EXCEL ONLY MUNICIPIOS
    date_df_municipios = (datetime.today().strftime('%d_%m_%Y'))
    df_municipios.to_excel('micodigopostal_municipios_' + date_df_municipios + '.xlsx', index=False)

else:
    print ("New municipios to add")
    enter = input("Enter to continue: ")
    print (compare_municipios)
    enter_2 = input("Do you want print the document in Excel ? y/n:")
    if (enter_2 == "y"):
        new_muni_date = (datetime.today().strftime('%d_%m_%Y'))
        compare_municipios.to_excel("new_municipios_" + new_muni_date +  ".xlsx", index=False)
        print ("The program have been finished, you must add new municipios on the folder all_links")
    else:
        print ("The program have been finished, you must add new municipios on the folder all_links")

