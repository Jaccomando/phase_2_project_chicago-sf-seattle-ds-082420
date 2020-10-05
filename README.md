# King County, WA Home Improvement Project

This project analyzes King County, WA home sales data to help home owners in King County determine which home improvement projects will increase the sale price of their homes.

## Directory Structure

### [Notebooks](https://github.com/Jaccomando/phase_2_project_chicago-sf-seattle-ds-082420/tree/master/notebooks)
This folder contains jupyter notebooks with exploratory data analyses and our final report notebook.

### [Reports](https://github.com/Jaccomando/phase_2_project_chicago-sf-seattle-ds-082420/tree/master/reports)
This folder contains a pdf of our slideshow presentation, and images used in the finalized presentation of the data.
  
### [References](https://github.com/Jaccomando/phase_2_project_chicago-sf-seattle-ds-082420/tree/master/refrences)
This folder conatains all relevant documentation for the data we used, and any documented informative references.

### [SRC](https://github.com/Jaccomando/phase_2_project_chicago-sf-seattle-ds-082420/tree/master/src)  
This folder includes code for all functions in the notebooks.

### [Instructions](https://github.com/Jaccomando/phase_2_project_chicago-sf-seattle-ds-082420/tree/master/instructions)
This folder contains the instructions and requirments for this project.

## Background
We set out to generate a multiple regression model to predict the effect of different improvements to homes on their sale value using the set of homes sold in 2019 in King County.

## Data Gathering

The data is downloaded with the get_dataframes() function. The get_tables function filters the data into the subset we want to study, and divides the features into features represented by continuous or ordinal values, ordtable and those that represent different categories of data, cattable.

## Data
We used data from the King County Assessor's free data catalog.

We filtered the data to include:
1. only single family homes
2. between \$200,000 and \$1,500,000
3. that are not designated as 'cabins'
  
We selected this range of home values because they are affordable to people earning between the median income of the lowest quintile of King County Earners, \$40,214 dollars, and the median income of the highest quintile of King County Earners, \$250,000, in 2018, according to [Kingcounty.gov](https://www.kingcounty.gov/independent/forecasting/King%20County%20Economic%20Indicators/Household%20Income/KC%20Household%20Income%20Quintiles.aspx) and [CNN Money's](https://money.cnn.com/calculator/real_estate/home-afford/index.html) home affordabilty calculator.

We also included a statistical test to determine whether converting a home into a duplex might increase the value per square foot. This would be helpful for homeowners to determine, depending on the size of their home, whether this renovation would be worth the cost.

![sales distribution](https://github.com/Jaccomando/phase_2_project_chicago-sf-seattle-ds-082420/blob/master/reports/figures/Sales_distribution.png?raw=true)

### Do Duplexes Sell for Less per Square Foot than Single Family Homes?
We start by answering this question with a T-Test.

First we state our null and alternative hypotheses, identify type 1 and type 2 errors, and set our alpha to .95.

Next we filter the data for the subset we want to explore and join the tables and extract the features we want to compare.

![duplex vs single family](https://github.com/Jaccomando/phase_2_project_chicago-sf-seattle-ds-082420/blob/master/reports/figures/duplex_v_single_family.png?raw=true)
 
In 2019 243 duplexes were sold, and 22804 single family homes were sold.
The mean cost per sqft of our samples for duplexes is 384.7626045951853.
The mean cost per sqft of our samples for single family homes is 348.4474482244218.
On average, duplexes sell for 36.315156370763475.


A quick glace at the sample means seems to indicate that, in fact, duplexes sell for about //$36 more per square foot than single family homes. 
We conduct a two sample, one-tailed Welch's test to determine the statistical significance of the difference in means. Our test confirs that we can be confident that duplexes sell for more per square foot than single family homes and that the difference is statistically significant.

## Multiple Regression Models
**Model 1:** Choosing the features to include is the most important part of building this model. We try using the ordinal features that directly correlate best with the sale price of the home. After running or model we see that it has some predictive power with an R2 of .452, but suffers from severe multicollinearity with a condition number of almost 30,000. Furthermore we conduct additional assumption testing including Homoskedasticity, Linearity, Normality and Independence (collinearity).

Model 1 is heteroskedastic because the residuals are not randomly distributed when plotted against our predicted sale prices. It passes the linear rainbow test for linearity by soundly rejecting the null hypothesis of non-linearity. It violates the normality assumption since the actual sample quantiles do not neatly map to the predicted quantiles. And it violates the assumption of independance indicating much collinearity between variables.

We can definitely improve upon this model!

**Model 2:** For Model 2 we use SciKitLearn's iterative algorithms to help us find the best features for our model. REFCV chooses both the best features based upon a recursive feature elimination method, as well as choosing the number of features to include.  Our R2 score improves to .459 and our condition number drops to more acceptable levels. As with Model 1, we conduct additional assumption tests.

Model 2 still fails Homoskedasticity by over estimating the value of lower value houses and under estimating the values of higher priced houses. It passes the linear rainbow test and is making linear predictions of the sale price vs the predictors. It violates the normality assumption as errors are not normally distributed. Our model does much better avoiding multi-collinearity, however some variables still have values over 5.

**Model 3:** For Model 3 we decide to assist REFCV by removing some features from consideration. We also suspect that some of the categorical variables from cattable may be predictive, so we let RFECV choose from a select set of those as well. Model 3 increases the R2 score to .464, and keeps the condition number low. It chooses 35 features to include and each one has a low p-value, and therefore a high degree of confidence in the significance of it's influence on the target. It's the best model yet, and the one we will keep! 

![homoskedasticity test](https://github.com/Jaccomando/phase_2_project_chicago-sf-seattle-ds-082420/blob/master/reports/figures/homoskedasticity_test.png?raw=true)

![normality graph](https://github.com/Jaccomando/phase_2_project_chicago-sf-seattle-ds-082420/blob/master/reports/figures/normality_graph.png?raw=true)

Model 3 passes the linear rainbow test for linearity with flying colors by soundly rejecting the null hypothesis of non-linearity. Our model does not violate the indepedence assumption. Our condition score is low, suggesting low multi-collinearity between features. The variance inflaction test showed that no feature scores above a 5 which confirms that our features are independent.

## Evaluation
The final model summary showed an improved goodness of fit with an R-squared of .464 meaning about 46% of the discrepancies in the dependent variable "Sales Price" are explained by the independent variables, or coefficients in our model.  There were 35 total features in the model that would help explain and increase or decrease to the value of the home aside from the original sales price of the property.  Building grade one of the most impactful can account for 131,000 dollars in the value of the home with a relatively small variance of about 2,000 dollars.  Another less impactful value used was the total square footage of the living space which could account for up to  84,000 dollars of the total home value with a variance of about 2,600 dollars.  However, not all of the coefficients used measured a postive impact, a forecosure on the property predicts a drop in the value of the property of about 185,600 dollars which may be of value to home flippers.

## Deployment
For the deployment of this model we have decided to create an app that can be used for home developers.  This app will allow the user to create a model of the home using known charachteristics and then as the user makes changes to the home, adding a new deck for instance, the app will tell the user what the change in home value will be. 
