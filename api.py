from flask import Flask
from flask_restful import Api, Resource
from fhir_parser.fhir import FHIR

app = Flask(__name__)
api = Api(app)
fhir = FHIR()

patients = fhir.get_all_patients()
#observations =

class Data(Resource):
    def __init__(self):
        super(Data, self).__init__()

    def get(self):
        '''Graph 1'''
        female_ages = []
        male_ages = []
        all_ages = []
        ages = {}

        for patient in patients:
            if str(patient.gender) == "female":
                female_ages.append(patient.age())
            if str(patient.gender == "male"):
                male_ages.append(patient.age())

        all_ages = female_ages + male_ages

        female_average = (sum(female_ages) / len(female_ages))
        male_average = (sum(male_ages) / len(male_ages))
        average = (sum(all_ages) / len(all_ages))

        ages = {'female_average':female_average, 'male_average':male_average, 'average':average}

        '''Graph 2'''
        counter = {}

        counter["Marriedmale"] = 0
        counter["Never Marriedmale"] = 0
        counter["Marriedfemale"] = 0
        counter["Never Marriedfemale"] = 0

        for patient in patients:
            gender = patient.gender
            marital_status = patient.marital_status
            #concatenate gender and marital status
            patient_info = str(marital_status) + str(gender)
            counter[patient_info] += 1

        '''Graph 3'''
        languages = {}

        for patient in patients:
            for language in patient.communications.languages:
                languages.update({language: languages.get(language, 0) + 1})

        returnData = {}
        returnData["married"] = counter
        returnData["languages"] = languages
        returnData["ages"] = ages

        return returnData


api.add_resource(Data, "/api/GoshFHIR/", endpoint="graph")


if __name__ == "__main__":
    app.run(debug=True, port=5002)