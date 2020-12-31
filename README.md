# Crème de la crème
## Investigating Metadata and Survivability of Top Android Apps

In this repository you will find all the notebooks used to perform the analysis. We divided the notebooks in three folders, one for each R,   each folder has 3 files:
- One for the dataset without imputations.
- One for the dataset with LOCF imputation
- One for the dataset with MFO imputation

Requirements:
- Python 3.6 or up
- Mongodb ([Install MongoDb Community Edition](https://docs.mongodb.com/manual/administration/install-community/)) 
- Pymongo
- Pandas and Numpy 
- SeaBorn and Matplotlib

In addition, there is a folder with the notebooks used to create the imputation datasets.

Steps to use the notebooks:
1. Download the dataset, from the links provided by of the authors.
2. Execute the script called _script_hall.py_, to add new fields to the collections.
3. Save the collection _app_ in a .csv file, to ease their use in the notebooks.
4. For notebooks of imputations, specific instructions are within the notebooks.
5. Include the Cliff's Delta implementation we used: https://github.com/neilernst/cliffsDelta
