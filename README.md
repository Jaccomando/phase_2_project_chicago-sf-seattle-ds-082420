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
