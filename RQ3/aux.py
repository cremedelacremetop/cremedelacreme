import pandas as pd
import numpy as np

def app_rebirth(row):
    """Counts how many times and appears and dissapears in the top
    
    paramaters
    ----------
    row:numpyArray
        A row from the pivot table
        
    returns
    -------
    count:int
        number of times that an app appears and dissapears in the top
    """
    count = 0
    appear = False
    
    for i in range(0,len(row)):
        if not appear and not np.isnan(row[i]) and row[i]==1 :
            appear = True
            count +=1
            #print(i)
        
        if (np.isnan(row[i]) or row[i] ==0 ) and appear:
            appear = False
    return count


def pivot_sum_top(dictionary, columns, country, df_summary_numbers, df_summary):
    """Creates a pivot table table vs date, inside a cell is 1 if it appears, 0 if not and NAN if are missing values.
       
       Params
       --------
       dictionary:dict
           Country dictionary that contains for a each possible category a DataFrame with the corresponding information
       columns:list
           List of all possible dates (weeks)
       country:str
           Country that is evaluated
       df_summary_numbers:DataFrame
           DataFrame  that contains the number of missing weeks for each country, category
       df_summary:DataFrame
           DataFrame that contains a list if with the weeks of  missing data for each country, category
       
       Returns 
       --------
       new_dict:dict
           Dictionary that cotains all the possible categories as keys and the value are dataFrames, that correspond to the pivot table ids vs weeks
       incomplete_category:int
           Number of categories with missing weeks (one or more)
    """
    new_dict = {}
    incomplete_category = 0
    set_columns = set(columns)
    
    for key, df in dictionary.items():
        pivot_table = pd.pivot_table(df, index= ['id'], columns= ['retrieved_date_end'], values= 'Flag')
        pivot_table.fillna(0,inplace= True)
        suum = pivot_table.sum(axis = 1)   
        pivot_table['sum'] = pivot_table.sum(axis = 1)   
        
        set_columns_dif = list(set_columns -set(pivot_table.columns) )
        
        if set_columns_dif:
            print(key)
            print(set_columns_dif)
            df_summary_numbers.at[key,country] = len(set_columns_dif)
            df_summary.at[key,country] = list(set_columns_dif)
            #df['CreationDate'].str.len()
            incomplete_category+=1
            pivot_table = pd.concat([pivot_table, pd.DataFrame(columns = set_columns_dif)],axis = 1, sort=False)
        
        
        pivot_table['occurrences'] = np.apply_along_axis(app_rebirth, 1, pivot_table[columns].values) 
        new_dict[key] = pivot_table[np.append(columns, ['sum','occurrences'])]
    
    return (new_dict, incomplete_category)

# Function to create for each possible category  a  dataFrame
def create_dataFrames_by_category(df, dictionary):
    for top, category in dictionary.keys():
        
        if category != '':
            dictionary[(top, category)] = df[:][(df.clean_category == category)&(df.top == top)]
        else:
            dictionary[(top, '')] = df[:][(df.top == top)]
            
def delete_flag (row, list_delete):
    """Marks all the rows that are part of an incomplete category
    """
    flag = 0
    
    for categories in list_delete:
        if categories[1]=='':
            if row['top'] == categories[0]:
                flag= 1
                return flag
        else:
            if row['top'] == categories[0] and row['clean_category'] == categories[1] :
                flag= 1
                return flag
    return 0

def pivot_sum_top_imp(dictionary, columns, country, df_summary_numbers, df_summary):
    """Creates a pivot table table vs date, inside a cell is 1 if it appears, 0 if not and NAN if are missing values.
       
       Params
       --------
       dictionary:dict
           Country dictionary that contains for a each possible category a DataFrame with the corresponding information
       columns:list
           List of all possible dates (weeks)
       country:str
           Country that is evaluated
       df_summary_numbers:DataFrame
           DataFrame  that contains the number of missing weeks for each country, category
       df_summary:DataFrame
           DataFrame that contains a list if with the weeks of  missing data for each country, category
       
       Returns 
       --------
       new_dict:dict
           Dictionary that cotains all the possible categories as keys and the value are dataFrames, that correspond to the pivot table ids vs weeks
       incomplete_category:int
           Number of categories with missing weeks (one or more)
    """
    new_dict = {}
    incomplete_category = 0
    set_columns = set(columns)
    
    for key, df in dictionary.items():
        pivot_table = pd.pivot_table(df, index= ['id'], columns= ['retrieved_date_end'], values= 'Flag')
        pivot_table.fillna(0,inplace= True)
        suum = pivot_table.sum(axis = 1)   
        pivot_table['sum'] = pivot_table.sum(axis = 1)   
        
        if  '2017-11-11' not in pivot_table.columns:
            pivot_table['2017-11-11']= 0
            
        set_columns_dif = list(set_columns -set(pivot_table.columns) )
        
        if set_columns_dif:
            print(key)
            print(set_columns_dif)
            df_summary_numbers.at[key,country] = len(set_columns_dif)
            df_summary.at[key,country] = list(set_columns_dif)
            #df['CreationDate'].str.len()
            incomplete_category+=1
            pivot_table = pd.concat([pivot_table, pd.DataFrame(columns = set_columns_dif)],axis = 1, sort=False)
        
        
        pivot_table['occurrences'] = np.apply_along_axis(app_rebirth, 1, pivot_table[columns].values) 
        new_dict[key] = pivot_table[np.append(columns, ['sum','occurrences'])]
    
    return (new_dict, incomplete_category)