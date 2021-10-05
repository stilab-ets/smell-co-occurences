import csv
import json
import os
from collections import Counter
import time

all_smells=['ClassDataShouldBePrivate','LazyClass','ComplexClass','LongParameterList','FeatureEnvy','LongMethod','BlobClass','MessageChain','RefusedBequest','SpaghettiCode','SpeculativeGenerality']

my_map = {}
path = "json_path"
list=[]
for element in os.listdir(path):
    if element.endswith(".json"):
        list.append(element)
#print(list)
for elm in list:
   with open(elm) as f_json:
       json_data = json.load(f_json)
   for entry in json_data:
       my_map[entry["fullyQualifiedName"]] = []

        #adding all class smells 
       for class_smell in entry["smells"] :
            my_map[entry["fullyQualifiedName"]].append(class_smell)

        #adding all methods smells  
       for method in entry["methods"] :
           for method_smell in method["smells"] :
               my_map[entry["fullyQualifiedName"]].append(method_smell)

time.sleep(50)
for element in os.listdir(path):
    element=element.replace(".json", "", 1)
    output1=element+".csv"
    with open(output1, 'w', newline='') as f_output:
        csv_output = csv.DictWriter(f_output, fieldnames=["Class", *all_smells], extrasaction='ignore', restval='0')
        csv_output.writeheader()
        for elem in my_map:
            smell_counts = Counter()
            smell_counts['Class'] = elem
            for smell in my_map[elem] :
                smell_counts[smell["name"]] += 1
                csv_output.writerow(smell_counts)
