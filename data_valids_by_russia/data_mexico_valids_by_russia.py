import pandas as pd

# READING ZIPCODES ANDREW
print ("Reading zipcode Andrew")
zipcodes_andrew = pd.read_excel("zipcodes_by_russia.xlsx", sheet_name='valids_by_russia')
zipcodes_andrew_two = zipcodes_andrew.drop(["City"], axis=1)
new_document_str = zipcodes_andrew_two.applymap(str)

# MICODIGOPOSTAL
print ("Reading micodigopostal tabla ")
all_zip_codes = pd.read_excel("micodigopostal_06_06_2022.xlsx", sheet_name='Sheet1')
all_zip_codes_str = all_zip_codes.applymap(str)

# MERGE ANDREW AND MICODIGOPOSTAL
print("Merge or compare Andrew with micodigopostal")
checking_all_zip = new_document_str.merge(all_zip_codes_str, how='outer', indicator='union')

# MICODIGOPOSTAL COMPARE WITH ANDREW
checking_all_zip_2 = checking_all_zip[checking_all_zip.union=='both']
micodigopostal_valid = checking_all_zip_2[['Estado', 'Municipio', 'Ciudad', 'Asentamiento','Codigo Postal']]

# CONCAT GEONAMES.ORG AND CODIGO-POSTAL.MX WITH MICODIGOPOSTAL
print ("Concat other zipcodes from geonames.org and codigo-postal.mx")
geonames_others = pd.read_excel("zipcodes_by_russia.xlsx", sheet_name='geonames_codigo-postal.mx')
geonames_others_str = geonames_others.applymap(str)
geonames_micodigopostal_valid = pd.concat([micodigopostal_valid, geonames_others_str])

# COMPARE GEONAMES.ORG AND CODIGO-POSTAL.MX WITH MICODIGOPOSTAL WITH ANDREW
print ("Merge all zipcodes to get the same zip codes of Andrew but with all information like , state, city, loclality etc..")
total_information = new_document_str.merge(geonames_micodigopostal_valid, how='outer', indicator='union')
total_information['Codigo Postal']= total_information['Codigo Postal'].str.rjust(5,'0')
total_information_final = total_information[['Estado', 'Municipio', 'Ciudad', 'Asentamiento','Codigo Postal', 'union']]

print ("Checking duplicates")
bool_series = total_information_final.duplicated()

# CHECK DUPLICATES
bool_series.to_excel('check_duplicates.xlsx')

print ("Print the document in Excel")
# DOCUMENT TOTAL
total_information_final.to_excel('data_mexico_valids_by_russia.xlsx')



