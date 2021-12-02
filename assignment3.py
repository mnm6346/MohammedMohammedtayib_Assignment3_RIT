class Physician: 
    __slots__ = ["__id", "__name", "__speciality"]
    def __init__(self, id, name, speciality):
        self.__name = name
        self.__id = id 
        self.__speciality = speciality

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_speciality(self):
        return self.__speciality

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def set_speciality(self, speciality):
        self.__speciality = speciality

    def __str__(self):
        return "Physician Name="+str(self.__name)
    
    def __repr__(self):
        return "    \n**Physician**\nId="+str(self.__id) \
        +"\nName="+self.__name\
        +"\nSpeciality="+self.__speciality





class Patient:
    __slots__ = ["__emr_id", "__name", "__gender", "__phone_number"]
    def __init__(self, em_id, name, gender, phone_no):
        self.__emr_id = em_id
        self.__name = name 
        self.__gender = gender 
        self.__phone_number = phone_no 

    def get_name(self):
        return self.__name

    def get_emid(self):
        return self.__emr_id

    def get_gender(self):
        return self.__gender
    
    def get_phoneno(self):
        return self.__phone_number

    def set_name(self, name):
        self.__name = name

    def set_emid(self, emid):
        self.__emr_id = emid

    def set_gender(self, gender):
        self.__gender = gender

    def set_phoneno(self, phone):
        self.__phone_number = phone

    def __str__(self):
        return "Patient Name="+self.__name

    def __repr__(self):
        return "    \n**Patient**\n"\
        +"ID="+str(self.__emr_id)\
        +"\nName="+self.__name\
        +"\nGender="+self.__gender\
        +"\nPhone Number="+str(self.__phone_number)





class Encounter:
    __slots__ = ["physician", "patient", "date", "disease", "medication"]
    def __init__(self, phy, pat, date, disease, med):
        self.physician = phy
        self.patient = pat 
        self.date = date 
        self.disease = disease
        self.medication = med

    def __repr__(self):
        return"    \n**Encounter**"\
        +"\n"+str(self.physician)\
        +"\n"+str(self.patient)\
        +"\ndate="+str(self.date)\
        +"\ndisease="+str(self.disease)\
        +"\nmedication="+str(self.medication)




import csv 
import random
patients = []


with open("patients.csv")as file:
    reader = csv.reader(file)
    for i in reader:
        patients.append(Patient(i[0],i[1],i[2],i[3]))

physician_obj = []
with open("Physician.csv") as file1:
    reader1 = csv.reader(file1)
    for z in reader1:
        physician_obj.append(Physician(z[0], z[1], z[2]))


disease = ["Headache", "Fever", "Flu", "Cough", "Diabetes"]
date = ["10-12-2021", "12-12-2020", "30-6-2021", "3-6-2021", "7-9-2021"]
medication = ["Panadol", "Acetaminophen", "Guaifenesin", "Dextromethorphan", "Insulin"] 


encounter1 = []
for e in range(5):
    encounter1.append(Encounter(physician_obj[random.randrange(3)],patients[e],date[e],disease[e],medication[e]))

print("-------------------------------------------------")
print(patients)
print("-------------------------------------------------")
print(physician_obj)
print("-------------------------------------------------")
print(encounter1)
print("-------------------------------------------------")
with open("encounter.csv","w") as file2:
    writer=csv.writer(file2)
    writer.writerow(encounter1)
    print()
    print("Added to encounter.csv successfully")
    print("-------------------------------------------------")




