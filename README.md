# Crème de la crème
## Investigating Metadata and Survivability of Top Android Apps

In this repository you will find all the notebooks used to perform the analysis. 

Each folder has 3 files:
- One for the dataset without imputations
- One for the dataset with LOCF imputation
- One for the dataset with MFO imputation

In addition, there is a folder with the notebooks used to create the imputation datasets.

To use the notebooks it is important to:
1. Download the dataset, from the links of the authors.
2. Execute the script called _script_hall.py_, to add new columns to the database.
3. Save the collection _app_ in a .csv file, to ease their use in the notebooks.
4. For notebooks of imputations, specific instructions are within the notebooks.
5. Include the Cliff's Delta implementation we used: https://github.com/neilernst/cliffsDelta
