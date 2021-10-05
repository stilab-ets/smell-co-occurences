# An Empirical Study on Code Smells Co-occurrences in Android Applications: Replication Package (IWoR 2021)
This repository contains all the material required to replicate our analysis, including (1) the data (2) the statistical analysis scripts, and (3) the analysis results.



Data collection
---------------
The data used for this study can be obtained by executing the scripts available in dataCollection folder: 

* githubCrawler.py: Mines Github repository for open-source, published apps.
* androidManifestChecker.py: Filters apps that do not have a corresponding Manifest file. 
* googlePlayPageChecker.py: Identifies the existence of Google Play Store page reported in links in repositories
* csvDuplicatesRemover.py: Removes duplicate entries from the csv.  
* appsCloning.py: clone the Github repository
* AndroidCodeSmellsDetection.py: Detects Android smells.
* OOCodesmellsDetection.py: Detects Object Oriented smells.
* JSONParser.py: Parses JSON files (returns of Organic) and converts them to CSV files.
* Merge.py: Merges CSV files. 

Analysis 
---------------
The totality of the statistical analysis scripts utilized for the study are available in Analysis folder: 

* aprioriAlgorithm.py: Calculates support, confidence and lift.
* RQ2_analysis.R: Performs all analysis related to RQ2.

Data
---------------
The data used for the analysis is available in Data folder where we found the list of apps and the detected traditional OO as well as Android smells.

Results 
---------------
The results produced in order to answer our research questions are provided in the results folder. 
