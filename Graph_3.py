from fhir_parser import FHIR

import numpy as np
import matplotlib.pyplot as plt
import requests

fhir = FHIR()
patients = fhir.get_all_patients()


url = "http://127.0.0.1:5002/api/GoshFHIR/"
returnData = requests.get(url).json()
languages = returnData["languages"]


plt.bar(range(len(languages)), list(languages.values()), align='center')
plt.xticks(range(len(languages)), list(languages.keys()), rotation='vertical')
plt.xlabel("Language")
plt.ylabel("Number of patients")
plt.title("Number of patients who speak the language")
plt.show()