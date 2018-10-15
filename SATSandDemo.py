import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}
ap_2010=pd.read_csv('schools/ap_2010.csv')
class_size=pd.read_csv('schools/class_size.csv')
demographics=pd.read_csv('schools/demographics.csv')
graduation=pd.read_csv('schools/graduation.csv')
hs_directory=pd.read_csv('schools/hs_directory.csv')
sat_results=pd.read_csv('schools/sat_results.csv')
data = {'ap_2010':ap_2010,'class_size':class_size,'demographics':demographics,
 'graduation':graduation,'hs_directory':hs_directory,'sat_results':sat_results}

 #Let's first begin by reading each file into a pandas dataframe, and then store
 #all of the dataframes in a dictionary. This will give us a convenient way to store them,
 #and a quick way to reference them later on.

print(data['sat_results'].head())
 #Quick preview of SAT data

for f in data:
    print(data[f].head())
#Loop through the first 5 rows of each data to gain a preview of each dataframe
#Each data set appears to either have a DBN column, or the information we need to create one. 
#That means we can use a DBN column to combine the data sets. First we'll pinpoint matching rows 
#from different data sets by looking for identical DBNs, then group all of their columns together 
#in a single data set.
#Some of the data sets appear to contain multiple rows for each school (because the rows have duplicate 
#DBN values). That means we’ll have to do some preprocessing to ensure that each DBN is unique 
#within each data set.

all_survey=pd.read_csv('schools/survey_all.txt',delimiter='\t',encoding='windows-1252')
d75_survey=pd.read_csv('schools/survey_d75.txt',delimiter='\t',encoding='windows-1252')

#Reading survey files into their individual dataframes before combining the two data together
#After combining both dataframes, we will take a quick preview before determing strategy.
survey=pd.concat([all_survey,d75_survey],axis=0)
survey.head()
#By looking at the output, there are over 2000 columns, nearly all of which we don't need. We'll have to filter 
#the data to remove the unnecessary ones. Working with fewer columns will make it easier to print the dataframe 
#out and find correlations within it.
#The survey data has a dbn column that we'll want to convert to uppercase (DBN). The conversion will make the 
#column name consistent with the other data sets.

survey['DBN']=survey['dbn']
column_list=["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", 
"eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]
survey=survey.loc[:,column_list]
#Filtered the survey dataframe by the the columns filters from the survey dictionary. Assigning the filtered dataframe
#back to the dictionary.

#Looking through the datasets, we can see that the 'class_size' dataframe does not have a DBN column. From looking at these rows, we can 
#tell that the DBN in the sat_results data is just a combination of the CSD and SCHOOL CODE columns in the class_size data. The main difference 
#is that the DBN is padded, so that the CSD portion of it always consists of two digits. That means we'll need to add a leading 0 to the CSD if 
#the CSD is less than two digits long.