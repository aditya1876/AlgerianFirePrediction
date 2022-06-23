# AlgerianFirePrediction

Predict the temperature and Fire based on data from Algerian Forests

##### Dataset - https://archive.ics.uci.edu/ml/datasets/Algerian+Forest+Fires+Dataset++

### Objectives

- import data
- EDA:
  - create detailed profile
  - perform graph based analysis
  - statistical insite from data
- preporcessing
  - handle missing values
  - encode categorical data
  - scale dataset if variation is high
  - handle outlier
  - handle multicolinearity
- Create classification and regression model
  - Regression model:
    - linear, ridge, lasso, SVR, Decision Tree Regressor, Random Forest Regressor
    - Cross validation and hyperparameter tuning
    - mse for each model
    - select best model based on R2 score
  - Classification model:
    - Logistic, SVM, DecisionTreeClassifier, naive bayes, Random forest classifier
    - crossvalidation and hyperparameter tuning
    - Classification report and select best model on the basis of the report
- Generic Tasks:
  - Create Flask API(postman) and HTML page
  - Perform single value prediction and bulk prediction
  - Data load via mongo DB or mysql(during bulk prediction)
  - Modular code
  - logging
  - handle exception at every step

#### Notes:

    - conda env - proj_algfire
