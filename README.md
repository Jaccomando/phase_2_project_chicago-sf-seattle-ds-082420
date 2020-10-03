# King County, WA Home Improvement Project

This project analyzes King County, WA home sales data to help home owners in King County determine which home improvement projects will increase the sale price of their homes. It uses data from 2019 home sales and makes recommendations on which home improvement projects provide the best return on investment (ROI).


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
Let's start with by answering this question with a T-Test.

Note, this dataset is not the same as for our multiple regression model.
We have included duplexes in this test, which are not present in the data for our regression model. Otherwise the price ranges and year sold are the same.

Hypotheses
Our null hypothesis is that duplexes do not sell for more per square foot than single family homes. Our alternative hypothesis is that they do sell for more than single family homes.

We will try to get results with a 95% confidence, so we will set our alpha to .95

Possible Errors:
If we make a type 1 error, we would claim that duplexes sell for more per square foot, when in reality they do not.
On the other hand, if we make a type 2 error, we would claim that they do not sell for more, when in fact they do.

First we filter the data for subset we want to explore. Next we join the tables and extract the features we want to compare.
### Single family vs duplex: sample size and sample means
In 2019 243 duplexes were sold, and 22804 single family homes were sold.
The mean cost per sqft of our samples for duplexes is 384.7626045951853
The mean cost per sqft of our samples for single family homes is 348.4474482244218
On average, duplexes sell for 36.315156370763475



A quick glace at the sample means seems to indicate that, in fact, duplexes sell for about //$36 more per square foot than single family homes. Let's test whether this difference is statistically significant, especially since our sample size of duplexes is much smaller than for single family homes.

Testing for statistical significance
We will be using a two sample, one-tailed Welch's test to determine the statistical significance of the difference in means. Our T-critical value tells us that we need a test statistic above 1.645 to confirm with 95% confidence that duplexes sell for more per square foot than single family homes. We are looking for a pvalue of .05 or less to confirm our result.

In fact, our test returns a test statistic of ~ 2.07 and our p-value is ~ .02. We can be confident that duplexes sell for more per square foot than single family homes and that the difference is statistically significant

