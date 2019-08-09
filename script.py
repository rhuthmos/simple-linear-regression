
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

def mymean(a):
	sum = np.sum(a.values)
	count = len(a.values)
	return(sum/count)
	
def mystd(a):
	q = np.square(a.values)
	sqsum = np.sum(q)
	count = len(a.values)
	mean = mymean(a)
	return((sqsum/count - (mean**2))**0.5)

def mycor(a,b):
	c = a.values*b.values
	nowsum = np.sum(c)
	count = len(c)
	mycov = (nowsum/count) - (mymean(a)*mymean(b))
	return(mycov/(mystd(a)*mystd(b)))
	
def linreg(x,y):
	coefficient = mycor(x,y)*mystd(y)/mystd(x)
	intercept = mymean(y) - coefficient*mymean(x)
	return coefficient,intercept
	
def myerror(yhat, yactual):
	k = len(yhat.values)
	output = 0
	for i in range(k):
		output = output + (yhat.values[i] - yactual.values[i])**2
	return (output/k)


if __name__ == "__main__":

	# preprocessing and reading journals data
	abc = pd.read_csv("found.txt",sep=";",header = None)
	abc.columns = ['Title', 'H-Index', 'Impact-Factor']
	abc_x = abc[["H-Index"]]
	abc_y = abc[['Impact-Factor']]

	# splitting journals data into training and test
	x_train,x_test,y_train,y_test = train_test_split(abc_x,abc_y,test_size = 0.2)

	coef,intercept = linreg(x_train,y_train)

	model = 'impact_factor=' + str(coef) + 'h_index+' + str(intercept)
	print("LinearRegression Model", model)

	yhat = coef*x_test + intercept	# finding impact factor for test data

	calculatedError = myerror(yhat,y_test)

	print ("root mean squared error", calculatedError)


	a= pd.read_csv('conf2.csv', sep=';')		# read original confrence data
	confData = a[['Title','H index']]
	confData.dropna(how = 'any')				# filtering

	# applying my regression model on h index of conferences

	L = []
	for i in range(len(confData[['H index']].values)):
		a = coef* confData[['H index']].values[i] + intercept
		L.append(a[0])
	confData.insert(2,"Impact-Factor",L,True)


	# writing conference data to excel file

	writer = pd.ExcelWriter('Output.xlsx')
	confData.to_excel(writer,'Sheet1')
	writer.save()
