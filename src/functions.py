#######################################################
import matplotlib.pyplot as plt
from math import ceil
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.ticker as mtick

from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

# using statsmodels
import statsmodels.formula.api as smf
import statsmodels.api as sm

%matplotlib inline
plt.style.use('ggplot')
from pandas.plotting import scatter_matrix
import pylab as py



#######################################################

def print_regression_summary(data,target,X,transformed_target=False):
    ''' Inputs:
    data -> dataframe that is being analyzed
    target -> String of column name for target variable
    X -> list of strings for independent variables
    transformed_target -> input True to log transform the target variable
    (ex. log transformed y)

    '''
    if transformed_target==False:
        indeps = data[X]
        y = data[target]
        indeps = sm.add_constant(indeps)
        model = sm.OLS(y,indeps).fit()
        predictions = model.predict(indeps)
        coeffs = model.params
        print(model.summary())
        return coeffs
    if transformed_target == True:
        indeps = data[X]
        y = np.log(data[target])
        indeps = sm.add_constant(indeps)
        model = sm.OLS(y,indeps).fit()
        predictions = model.predict(indeps)
        coeffs = model.params
        print(model.summary())
        return coeffs
    else:
        None


if __name__ == "__main__":
    pass