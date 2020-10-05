from io import BytesIO, TextIOWrapper, StringIO
from zipfile import ZipFile
import pandas as pd
import requests
import numpy as np
import scipy
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from statsmodels.regression.linear_model import GLS
from statsmodels.stats.diagnostic import linear_rainbow
from statsmodels.stats.outliers_influence import variance_inflation_factor

def produce_model(data, target):
    '''
    takes data as a dataframe of predictors with a target, takes target as a string equal to the column name
    of the target in data.
    returns the model generated from smf.ols().fit()
    '''
    preds = f'{target} ~ ' + str(data.loc[ : , data.columns != target].columns[0])
    for pred in data.loc[ : , data.columns != target].columns[1:]:
        preds = preds + f' + {pred}'
    formula = preds

    model = smf.ols(preds, data).fit()
    return model

def make_heatmap(data):
    '''
    produces a correlation heatmap from a pandas dataframe, returns an ax object containing the graph
    '''
    mask = np.triu(np.ones_like(data.corr(), dtype=np.bool))
    fig, ax = plt.subplots(figsize = (15,10))
    plt.xticks(fontsize = 10)
    plt.yticks(fontsize = 10)
    sns.heatmap(data.corr(), mask= mask, ax= ax, cmap = 'viridis')
    return ax

def homoskedasticity_test(model):
    '''
    given a regression model, this fucntion prints a homoskedasticity test as a scatter plot to notebook output
    '''
    y_hat = model.predict()
    fig = sns.scatterplot(x = y_hat, y = model.resid)
    plt.show()

def rainbow_stats(model):
    '''
    given a regression model, this function returns the values from a rainbow test stored as a dictionary
    '''
    rainbow_statistic, rainbow_p_value = linear_rainbow(model)
    return {'rainbow_stat': rainbow_statistic, 'rainbow_p_value': rainbow_p_value}

def normality_graph(model):
    '''
    given a regression model, this function prints a normality graph to notebook output
    '''
    fig = sm.graphics.qqplot(model.resid, dist = scipy.stats.norm, line = '45', fit=True)
    plt.show()

def colinearity_testing(predictors):
    '''
    given a dataframe containing all predictors in a model excluding the target, returns a dataframe containing the
    variance inflation factors for each predictive feature
    '''
    rows = predictors.values

    vif_df = pd.DataFrame()
    vif_df["VIF"] = [variance_inflation_factor(rows, i) for i in range(len(predictors.columns))]
    vif_df["feature"] = predictors.columns

    return vif_df

def check_assumptions(model, predictors):
    '''
    takes in a linear model and a dataframe of predictors (do not include target in predictors dataframe)
    return: none, this function only prints all assumption test results to the notebook output
    '''
    homoskedasticity_test(model)
    print(rainbow_stats(model))
    normality_graph(model)
    print(colinearity_testing(predictors))

    
def tt_ind(sample1, sample2, alpha = .05, equal_var = True, tails = 2):
    """
    Takes 2 array-like objects, sample1 and sample 2: samples to test for difference
    and 1 float: the level of confidence, alpha (default .05)
    and 1 bool: whether samples have equal variances (default True)
    and a number of tails: 1 or 2 (default 2)
    performs two sample t-test and prints critical stat, test stat, and one-tailed pvalue
    """
    import scipy.stats as stats

    tcrit = stats.t.ppf(q=.05, df = len(sample1) + len(sample2)-1)
    tstat = stats.ttest_ind(sample1, sample2, equal_var = equal_var)
    if tails == 1:
        print(f'critical stat is {tcrit}, test stat is {tstat[0]} with a pvalue of {tstat[1]/2}')
    elif tails == 2:
        print(f'critical stat is {tcrit}, test stat is {tstat[0]} with a pvalue of {tstat[1]}')
    else:
        print('Please set tails to either 1 or 2')


def cohen_d(sample1, sample2):
    """
    Takes 2 array-like objects: samples to compare
    Returns a float: the standard effect size according to the Cohen D equation.
    """
    import numpy as np
    effect_size = (sample1.mean() - sample2.mean()) / np.sqrt(((len(sample1) -1) * sample1.var()
                                                         + len(sample2) -1 * sample2.var()
                                                          / len(sample1) + len(sample2) -2))
    return effect_size