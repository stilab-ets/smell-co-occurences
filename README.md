# An Empirical Study on Code Smells Co-occurrences in Android Applications: Replication Package (IWoR 2021)
This repository contains all the material required to replicate our analysis, including (1) the data (2) the statistical analysis scripts, and (3) the analysis results.



Data collection
---------------
The data used for this study can be obtained by executing the scripts available in Data Collection folder: 

1. [githubCrawler.py](https://github.com/stilab-ets/smell-co-occurences/blob/main/dataCollection/githubCrawler/githubCrawler.py-Mines) - Mines Github repository for open-source, published apps.
2. [androidManifestChecker.py](https://github.com/stilab-ets/smell-co-occurences/blob/main/dataCollection/AndroidManifestChecker/androidManifestChecker.py) - Filters apps that do not have a corresponding Manifest file. 
3. [googlePlayPageChecker.py](https://github.com/stilab-ets/smell-co-occurences/blob/main/dataCollection/googlePlayPageChecker/googlePlayPageChecker.py) - Identifies the existence of Google Play Store page reported in links in repositories
4. [csvDuplicatesRemover.py](https://github.com/stilab-ets/smell-co-occurences/blob/main/dataCollection/csvDuplicatesRemover/csvDuplicatesRemover.py) - Removes duplicate entries from the csv.  
5. [appsCloning.py](https://github.com/stilab-ets/smell-co-occurences/blob/main/dataCollection/AppsCloning/clone.py) - Clones the Github repository
6. [AndroidCodeSmellsDetection.py](https://github.com/stilab-ets/smell-co-occurences/tree/main/dataCollection/AndroidCodeSmellsDetection) -  Detects Android smells.
7. [OOCodesmellsDetection.py](https://github.com/stilab-ets/smell-co-occurences/blob/main/dataCollection/OOCodesmellsDetection/OOCodesmellsDetection.py) - Detects Object Oriented smells.
8. [JSONParser.py](https://github.com/stilab-ets/smell-co-occurences/blob/main/dataCollection/JSONParser/JSONParser.py) - Parses JSON files (returns of Organic) and converts them to CSV files.
9. [Merge.py](https://github.com/stilab-ets/smell-co-occurences/blob/main/dataCollection/Merge/merge.py) - Merges CSV files. 

Analysis 
---------------
The totality of the statistical analysis scripts utilized for the study are available in Analysis folder: 

1. [aprioriAlgorithm.py](https://github.com/stilab-ets/smell-co-occurences/blob/main/Analysis/aprioriAlgorithm.py) - Calculates support, confidence and lift.
2. [RQ2_analysis.R](https://github.com/stilab-ets/smell-co-occurences/blob/main/Analysis/RQ2_analysis.R) - Performs all analysis related to RQ2.

Data
---------------
The data used for the analysis is available in Data folder where we found the list of apps and the detected traditional OO as well as Android smells [here](https://github.com/stilab-ets/smell-co-occurences/tree/main/Data)

Results 
---------------
The results produced in order to answer our research questions are provided in the results folder [here](https://github.com/stilab-ets/smell-co-occurences/tree/main/Results)

## How to cite?

Please, use the following bibtex entry:

```
@inproceedings{Hamdi2021smells,
  title={An Empirical Study on Code Smells Co-occurrences in Android Applications},
  author=Hamdi, Oumayma and Ouni, Ali and AlOmar, Eman Abdullah and Mkaouer, Mohamed Wiem},
  booktitle={36th IEEE/ACM International Conference on Automated Software Engineering (ASE '21)},
  pages={1--8},
  year={2021}
}
``` 
