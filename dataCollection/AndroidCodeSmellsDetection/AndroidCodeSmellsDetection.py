import os
import os.path
import shlex, subprocess
import git
import pandas as pd
os.chdir('aDoctor_path')
retval = os.getcwd()
pathp= "projects_path/"

for element in os.listdir(pathp):

    path= pathp+"/"+element
    outversion = "outversionn_path/"+ "out"+element+".csv"
    cmd='java -cp aDoctor-1.0.jar it.unisa.aDoctor.process.RunAndroidSmellDetection %s %s "111111111111111"'
    cmd = cmd % (path,outversion)
    args = shlex.split(cmd)
    p = subprocess.Popen(args)
    
