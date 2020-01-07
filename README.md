# Shapley
Implementation of Shapely Owen decomposition used in Multiple regression models.

## Getting started 
Quite often we would like to understand how the role of each independent variable in the overall model.A simpler way of doing this is by decomposing the R-Squared using the Shapley Owen decomposition

## Installation
  ````pip install shapley````
  
## Attributes
coeff_ :dictionary  of shape (n_features,)  
        Estimated coefficients for the Shapley Owen  problem.
        
## Example
````
import pandas as pd
from Shapley import ShapleyValues

working_data = pd.read_csv('Shapely_input2.csv')
X = working_data[working_data.columns.difference(['Y'])]
Y = working_data[['Y']]
Sp = ShapleyValues()
Shapley_Values =Sp.fit(X,Y)
print (Shapley_Values.coef_)

{'X1': 0.0010701967805290535, 'X2': 0.010827740911131756, 'X3': 0.0024885120812901951, 'X4': 2.8260328860385538e-05}
````
