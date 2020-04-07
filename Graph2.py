from fhir_parser import FHIR

# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import requests

fhir = FHIR()
patients = fhir.get_all_patients()

url = "http://127.0.0.1:5002/api/GoshFHIR/"
returnData = requests.get(url).json()
data = returnData["married"]


# y-axis in bold
rc('font', weight='bold')

# Values of each group
values = {'brownBars': [data["Marriedfemale"], data["Marriedmale"]], 'greenBars': [data["Never Marriedfemale"], data["Never Marriedmale"]]}
df = pd.DataFrame(values)
'''total_females = []
total_males = []
for i in range(0, len(df['brownBars'])):
    total_females.append(sum(df['brownBars']))
for j in range(0, len(df['greenBars'])):
    total_males.append(sum(df['greenBars']))'''
total_patients = [i + j for i, j in zip(df['brownBars'], df['greenBars'])]
brownBars = [i / j * 100 for i, j in zip(df['brownBars'], total_patients)]
greenBars = [i / j * 100 for i, j in zip(df['greenBars'], total_patients)]

# Heights of bars1 + bars2
bars = np.add(brownBars, greenBars).tolist()

# The position of the bars on the x-axis
r = [0, 1]

# Names of group and bar width
names = ['Female', 'Male']
barWidth = 0.7

# Create brown bars
plt.bar(r, brownBars, color='#4DB2B5', edgecolor='white', width=barWidth, label="Married")
# Create green bars (middle), on top of the first ones
plt.bar(r, greenBars, bottom=brownBars, color='#8FC8AE', edgecolor='white', width=barWidth, label="Single")


# Custom X axis
plt.xticks(r, names, fontweight='bold')
plt.xlabel("Gender")
plt.ylabel("Percentage of Patients")
plt.title("Proportions of males and females who are single/married")

# Add a legend
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)

# Show graphic
plt.show()








