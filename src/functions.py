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


plt.style.use('ggplot')
from pandas.plotting import scatter_matrix
import pylab as py



#######################################################


#######################################################

def print_regression_summary(data,target,X,transformed_target=False):
    ''' Inputs:
    data -> csv file of data being analyzed from cleaned_data directory
    target -> String of column name for target variable
    X -> list of strings for independent variables
    transformed_target -> input True to log transform the target variable
    (ex. log transformed y)

    '''
    data_df = pd.read_csv("../cleaned_data/"+data)
    if transformed_target==False:
        indeps = data_df[X]
        y = data_df[target]
        indeps = sm.add_constant(indeps)
        model = sm.OLS(y,indeps).fit()
        predictions = model.predict(indeps)
        coeffs = model.params
        print(model.summary())
        return coeffs
    if transformed_target == True:
        indeps = data_df[X]
        y = np.log(data_df[target])
        indeps = sm.add_constant(indeps)
        model = sm.OLS(y,indeps).fit()
        predictions = model.predict(indeps)
        coeffs = model.params
        print(model.summary())
        return coeffs
    else:
        None

def interpret_regression_coeffs(coeffs):
    """
    Interpret the coefficients from a StatsModels linear regression.

    Parameters:
    - coeffs -> print_regression_function

    Prints:
    - Interpretation of each coefficient in a user-friendly format.
    """
    for param, coeff in coeffs.items():
        print(f"The coefficient for '{param}' is {coeff:.4f}.")
        if coeff > 1 and param != 'const':
            print(f"A one billion dollar increase in '{param}' is associated with an increase of ${coeff:.4f} in GDP per Capita.")
        elif 1 > coeff > 0 and param != 'const':
             print(f"A one billion dollar increase in '{param}' is associated with an increase in GDP per Capita by {coeff:.4f}%")
        elif 0 > coeff > -1 and param != 'const':
             print(f"A one billion dollar increase in '{param}' is associated with an decrease in GDP per Capita by {abs(coeff):.4f}%")
        elif coeff < 0 and param != 'const':
            print(f"A one billion dollar increase in '{param}' is associated with a decrease of {abs(coeff):.4f} in GDP per Capita.")
        else:
            print(f"'{param}' has no effect on the dependent variable.")
        
        print()



if __name__ == "__main__":
    # print_regression_summary('gdp_gov_spending.csv','GDP_Per_Capita',['Defense'])
    results = print_regression_summary('gdp_gov_spending.csv','GDP_Per_Capita',['Defense','NonDefense','State_Local'],True)
    interpret_regression_coeffs(results)