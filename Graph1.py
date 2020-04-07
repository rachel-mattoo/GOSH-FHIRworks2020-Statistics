from fhir_parser import FHIR

# libraries
import matplotlib.pyplot as plt
import requests

fhir = FHIR()
patients = fhir.get_all_patients()

url = "http://127.0.0.1:5002/api/GoshFHIR/"
returnData = requests.get(url).json()
ages = returnData["ages"]

barWidth = 0.7

x = ["Female", "Male", "Overall"]
y = [ages['female_average'], ages['male_average'], ages['average']]
plt.barh(x, y, height=barWidth, color = "#B69FEC")
plt.xlim(40, 45)
plt.xlabel("Average age")
plt.title("Average age by gender")
plt.show()

'''for index, value in enumerate(y):
    plt.text(value, index, str(value))'''
'''observations = []

for patient in patients:
    observations.extend(fhir.get_patient_observations(patient.uuid))

observation_types = [observation.type for observation in observations]


observations_dict = {}
for patient in patients:
    for observation_type in observation_types:
        observations_dict.update({observation_type: observations_dict.get(observation_type, 0) + 1})

plt.bar(range(len(observations_dict)), list(observations_dict.values()), align='center')
plt.xticks(range(len(observations_dict)), list(observations_dict.keys()), rotation='vertical')
plt.show()'''











