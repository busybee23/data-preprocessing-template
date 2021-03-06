#IMPORTING THE LIBRARIES 

import numpy as np #for mathematical operations like liner al, fourier transformation
import matplotlib.pyplot as mpl  #for graph representation 
import pandas as pd #for importing dataset and working with it

#IMPORTING DATASET
#data.csv file should be present in the folder where this script is saved

#decalaring a variable "DATASET"
dataset = pd.read_csv("data.csv")
#pd.read_csv imports the data file 
#datset imported succesfully 

#Seprating independent and dependent variable 
#Indepent Var are country, age, salary here
#Dependent are which we want to know from machine, i;e yes/no 

X = dataset.iloc[:,:-1].values
#X is for columns extraction [:,:-1] this takes all rows that is all 10 members
#and -1 leaves last column while including all the columns

Y = dataset.iloc[:,3].values
#Y takes the last columns by using its index 3 and all rows of that column
#DON'T FORGET THE VALUES IN Y AND X 

#___________________________________________________________________________________________________#

#MISSING DATA TREATMENT 

from sklearn.impute import SimpleImputer
#simpleImpute is the new Imputer and is used to fill the missing data (mathematically)
#we have imported a class now lets create and object of that class "IMPUTER"
imputer = SimpleImputer(missing_values = np.nan , strategy = "most_frequent")
#here missing values are denoted by nan is our data set and strategy is which way we want to fill it
imputer = imputer.fit(X[:,1:3])
#here we fit the value in place of nan
X[:,1:3] = imputer.transform(X[:,1:3])


#_____________________________________________________________________________________________________#

"""
ENCODING CATEGORICAL DATA 
LabelEncoder = france, spain, germany into numerics
Problem with label encoding is that it assumes higher the categorical value, better the category
OneHotEncoder(converts to binary) =  https://hackernoon.com/what-is-one-hot-encoding-why-and-when-do-you-have-to-use-it-e3c6186d008f

"""
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
one_hot_encoder = OneHotEncoder()
le = LabelEncoder()

X[:,0] = le.fit_transform(X[:,0])
Y = le.fit_transform(Y)
ct = ColumnTransformer([('one_hot_encoder', OneHotEncoder(), [0])],remainder='passthrough')
# The column numbers to be transformed (here is [0] but can be [0, 1, 3])
X = np.array(ct.fit_transform(X), dtype=np.float)

"""
OneHotEncoder will create k number of columns if there are k classes for a single variable.
For example : it will create 2 variables if gender values in that dataset are Male/Female, It will create 3 Variables if gender values are male/Female/PreferNotToSay
Now, You don't want multiple variables in your predicate y, So better go with LabelEncoder(from sklearn.preprocessing) or some mechanism that keeps the dimensionality intact.
"""

#TRAIN TEST SPLIT
#sklearn.cross_validation has been deprecated 
from sklearn.model_selection import train_test_split  
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state=0)

"""
X train contains what data will be in the traning section 
test_size = 0.2 means 20% of data, so here 2 rows will be in test, rest will be used for training
0.2-04 is the range of test wherer 0.25 is most used 

"""

#gonna add some basic youtube videos for this and for every code here on git just of refrence purposes





















