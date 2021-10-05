import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
import time
import pandas as pd

store_data = pd.read_csv('Path_to_your_dataset')
print(store_data.shape)
records = []

time.sleep(10)
for i in range(0, 1827):
    records.append([str(store_data.values[i,j]) for j in range(0, 24)])
    for i,j in enumerate(records):
        while 'nan' in records[i]:
            records[i].remove('nan')
association_rules = apriori(records, min_support=0.07, min_confidence=0.5, min_lift=1, min_leverge=1, max_length=2, use_colnames=True)
association_results = list(association_rules)
print(len(association_results))
print(association_results)




