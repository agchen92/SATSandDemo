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