# King County, WA Home Improvement Project

This project analyzes King County, WA home sales data to help home owners in King County determine which home improvement projects will increase the sale price of their homes.


## Background
We set out to generate a multiple regression model to predict the effect of different improvements to homes on their sale value using the set of homes sold in 2019 in King County.

## Data
We used data from the King County Assessor's free data catalog.

We filtered the data to include:
1. only single family homes
2. between \$200,000 and \$1,500,000
3. that are not designated as 'cabins'
  
We selected this range of home values because they are affordable to people earning between the median income of the lowest quintile of King County Earners, \$40,214 dollars, and the median income of the highest quintile of King County Earners, \$250,000, in 2018, according to [Kingcounty.gov](https://www.kingcounty.gov/independent/forecasting/King%20County%20Economic%20Indicators/Household%20Income/KC%20Household%20Income%20Quintiles.aspx) according to [CNN Money's](https://money.cnn.com/calculator/real_estate/home-afford/index.html) home affordabilty calculator.

We also included a statistical test to determine whether converting a home into a duplex might increase the value per square foot. This would be helpful for homeowners to determine, depending on the size of their home, whether this renovation would be worth the cost.

## Data Gathering

The data is downloaded with the get_dataframes() function. The get_tables function filters the data into the subset we want to study, and divides the features into features represented by continuous or ordinal values, ordtable and those that represent different categories of data, cattable.

### Do Duplexes Sell for Less per Square Foot than Single Family Homes?
We started by answering this question with a T-Test.

First we stated our null and alternative hypotheses, identified type 1 and type 2 errors, and set our alpha to .95

Next we filtered the data for the subset we wanted to explore and joined the tables and extracted the features we wanted to compare.

In 2019 243 duplexes were sold, and 22804 single family homes were sold.
The mean cost per sqft of our samples for duplexes is 384.7626045951853.
The mean cost per sqft of our samples for single family homes is 348.4474482244218.
On average, duplexes sell for 36.315156370763475.


A quick glace at the sample means seems to indicate that, in fact, duplexes sell for about //$36 more per square foot than single family homes. 
We conducted a two sample, one-tailed Welch's test to determine the statistical significance of the difference in means. Our test confirmed that we can be confident that duplexes sell for more per square foot than single family homes and that the difference is statistically significant.

## Multiple Regression Models
Model 1: Choosing the features to include was the most important part of building this model. We tried using the ordinal features that directly correlated best with the sale price of the home. After running or model we saw that it had some predictive power with an R2 of .452, but suffered from sever multicollinearity with a condition number of almost 30,000. Furthermore we conducted additional assumption testing including Homoskedasticity, Linearity, Normality and Independence (collinearity).

Model 1 was heteroskedastic because the residuals were not randomly distributed when plotted against our predicted sale prices. It passed the linear rainbow test for linearity by soundly rejecting the null hypothesis of non-linearity. It violated the normality assumption since the actual sample quantiles did not neatly map to the predicted quantiles. And it violated the assumption of independance indicating much collinearity between variables.

We can definately improve upon this model!


