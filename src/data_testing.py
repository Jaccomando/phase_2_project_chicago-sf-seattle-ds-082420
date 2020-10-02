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
    mask = np.triu(np.ones_like(data.corr(), dtype=np.bool))
    fig, ax = plt.subplots(figsize = (15,10))
    plt.xticks(fontsize = 10)
    plt.yticks(fontsize = 10)
    sns.heatmap(data.corr(), mask= mask, ax= ax, cmap = 'viridis')
    return ax

def homoskedasticity_test(model):
    y_hat = model.predict()
    fig = sns.scatterplot(x = y_hat, y = model.resid)
    plt.show()

def rainbow_stats(model):
    rainbow_statistic, rainbow_p_value = linear_rainbow(model)
    return {'rainbow_stat': rainbow_statistic, 'rainbow_p_value': rainbow_p_value}

def normality_graph(model):
    fig = sm.graphics.qqplot(model.resid, dist = scipy.stats.norm, line = '45', fit=True)
    plt.show()

def colinearity_testing(predictors):
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