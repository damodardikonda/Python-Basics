df_excel=pd.read_excel('Excel_Sample.xlsx')
df_excel.head()

#Pickling
#All pandas objects are equipped with to_pickle methods which use Python’s
# cPickle module to save data structures to disk using the pickle format.


df_excel.to_pickle('df_excel') # converting to pickle

df=pd.read_pickle('df_excel')#reading pickle file

print(df.head())#print 1st 5 files
