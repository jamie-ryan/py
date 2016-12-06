#Regression - intro
import pandas as pd
import quandl
import math
import numpy as np
#for scaling, sorting and support vector machine (for the regression)
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

#get data from quandl
df = quandl.get("WIKI/GOOGL")

#show data head
#print(df.head())
#Adjusted data are those stock prices which have been adjusted to cater
#for the seller splitting a bunch of stocks to make them cheaper
#i.e., 10 stocks at £100 each being turned into 20 at £50 each.


#define data vie header titles 
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
#high low percentage
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100
#percentage change
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100

#features
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]
#show data
#print(df.head())
#is Adj. Close a regression feature or a label? - feature
#Feature (machine learning)
#In machine learning and pattern recognition, a feature is an individual measurable
#property of a phenomenon being observed. Choosing informative, discriminating and
#independent features is a crucial step for effective algorithms in pattern
#recognition, classification and regression

#Label could be a future price

forecast_col = 'Adj. Close'
#fill empty data slots... can't use nan values in machine learning
#-99999 is treated as an outlier
df.fillna(-99999, inplace=True)

#math.ceil rounds up to the nearest integer
#0.1*len(df) is basically saying use the price from ten days ago to predict the price tomo
forecast_out = int(math.ceil(0.01*len(df)))

#label
#shift the column 
#comparing the forecast price to the adjusted close price
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.head())
print(df.tail())

#now we're ready to test and train a classifier

#features are X, labels are y
#drop the label column... everything except the label column
X = np.array(df.drop(['label'],1))
#labels
y = np.array(df['label'])

#scale X (-1 to 1) b4 we feed it through the classifier
#in reality all data would need to be scaled, which in high frequency stock
#analysis, would take too much time and thus this step would be omitted by traders.
X = preprocessing.scale(X)

X = X[:-forecast_out+1]
df.dropna(inplace=True)
y = np.array(df['label'])

print(len(X),len(y))







