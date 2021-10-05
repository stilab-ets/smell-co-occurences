import os
import shlex
import subprocess
import pandas as pd
path='C:/Users/AQ42770/Documents/co-occurences'
os.chdir(path)
df=pd.read_csv('324_analysed_apps.csv' ,sep=',')
repo_Name = df['Link']
b=repo_Name.to_frame(name=None)
#print(b)

    

a='https://github.com/'
for elem in b['Link']:
    a1=str(a)+str(elem)
    print(a1)
    commande='git clone --depth 1 %s'
    commande= commande % (a1)
    args = shlex.split(commande)
    p = subprocess.Popen(args)

        
    
    
    
    

