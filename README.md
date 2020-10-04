## Table of Contents

### Notebooks
This folder contains notebooks with exploratory data analyses.

### Reports
This folder contains finalized notebooks, a slideshow presentation, and images used in the finalized presentation of the data.
  
### References
This folder conatains all relevant information uesd to create our finalized reports including the .csv files containing the data tables, lookup docs for the tables themselves, and any documented informative references.

### [SRC](https://github.com/Jaccomando/phase_2_project_chicago-sf-seattle-ds-082420/tree/master/src)  
This folder includes code for all functions in the notebooks.


## Evaluation
The final model summary showed an improved goodness of fit with an R-squared of .464 meaning about 46% of the discrepancies in the dependent variable "Sales Price" are explained by the independent variables, or coefficients in our model.  There were 35 total features in the model that would help explain and increase or decrease to the value of the home aside from the original sales price of the property.  Building grade one of the most impactful can account for 131,000 dollars in the value of the home with a relatively small variance of about 2,000 dollars.  Another less impactful value used was the total square footage of the living space which could account for up to  84,000 dollars of the total home value with a variance of about 2,600 dollars.  However, not all of the coefficients used measured a postive impact, a forecosure on the property predicts a drop in the value of the property of about 185,600 dollars which may be of value to home flippers.

## Deployment
For the deployment of this model we have decided to create an app that can be used for home developers.  This app will allow the user to create a model of the home using known charachteristics and then as the user makes changes to the home, adding a new deck for instance, the app will tell the user what the change in home value will be. 
