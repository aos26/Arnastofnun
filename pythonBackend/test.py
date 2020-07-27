import requests
import pandas as pd
import math



BASE = "http://127.0.0.1:5000/"

#words = pd.read_csv(r'C:\Users\alext\CodeStuff\Arnastofnun\pythonBackend\gogn.csv', sep=';', error_bad_lines=False, encoding='ISO 8859-15')

#words = words.dropna(subset=['texti'])
# DELETE
#response = requests.delete(BASE + "words/1")
#print(response.json)
response = requests.get(BASE + "words/549")
print(response.json())

#response = requests.put(BASE + "words/" + str(0), { "flid": words['flid'].values[0], "ord": words['ord'].values[0], "ordflokkur": words['ordflokkur'].values[0], "texti": words['texti'].values[0], "fjoldi_risamalheild": words['fjoldi_risamalheild'].values[0], "fjoldi_ritmalssafn": words['fjoldi_ritmalssafn'].values[0]})
#print( { "flid": words['flid'].values[1], "ord": words['ord'].values[1], "ordflokkur": words['ordflokkur'].values[1], "texti": words['texti'].values[1], "fjoldi_risamalheild": words['fjoldi_risamalheild'].values[1], "fjoldi_ritmalssafn": int(words['fjoldi_ritmalssafn'].values[2])})
#print(response.json())
"""for i in range(len(words)):
    if math.isnan(words['fjoldi_ritmalssafn'].values[i]):
        response = requests.put(BASE + "words/" + str(i), { "flid": words['flid'].values[i], "ord": words['ord'].values[i], "ordflokkur": words['ordflokkur'].values[i], "texti": words['texti'].values[i], "fjoldi_risamalheild": words['fjoldi_risamalheild'].values[i], "fjoldi_ritmalssafn": 0})
    else:
        response = requests.put(BASE + "words/" + str(i), { "flid": words['flid'].values[i], "ord": words['ord'].values[i], "ordflokkur": words['ordflokkur'].values[i], "texti": words['texti'].values[i], "fjoldi_risamalheild": words['fjoldi_risamalheild'].values[i], "fjoldi_ritmalssafn": int(words['fjoldi_ritmalssafn'].values[i])})
    print(response.json())
"""

#print(words['flid'].values[0])

#response = requests.get(BASE + "wordfetcher/Alex/25")
#print(response.json())