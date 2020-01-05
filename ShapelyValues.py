
# coding: utf-8

# In[ ]:



# In[1]:

from itertools import combinations
import re
from sklearn.linear_model import LinearRegression
import math
import pandas as pd
import numpy as np
from scipy import stats

# In[2]:

class Shapely():
    def __init__(self):
        pass
    
    def fit(self,X,y):
        idx_list = [i for i in range(1,len(X.columns)+1)]
        column_map = dict(zip(X.columns,idx_list))
        working_X =X.rename(columns=column_map)
        RSquared_Dict = Combos_R_Squared(working_X,y)
        Shapely_dict = Shapely_weights(RSquared_Dict,len(X.columns))
        Shapely_values ={k: Shapely_dict[v] for k, v in column_map.items()}
        self.coef_ = Shapely_values
        return self

#Getting all possible combinations
def Combos_list(X):
        combos=[]
        for i in range(len(X)+1):
            comb = combinations(X,i)
            for i in comb:
                combos.append(i)
        return combos

#Calculating R-squared for all combinations
def Combos_R_Squared(X,Y):
    combos = Combos_list(X.columns)
    RSquared_Dict = {'':0} # Declared the R^2 when no  Channel is involved
    for i in combos:
        curr_combo = list(i)
        if len(i) > 0:
            x = X[curr_combo] # All combos of  channels are pased iteratively('display_event', 'email', 'paid_search', 'social_media')
            regressor = LinearRegression() 
            regressor.fit(x, Y)
            regressor.score(x, Y)
            RSquared_Dict[''.join([str(elem) for elem in curr_combo]) ] = regressor.score(x, Y)
    return RSquared_Dict

def Shapely_weights(RSquared,n):
    Shapely_dict ={}
    idx_list = [i for i in range(1,n+1)]
    for i in idx_list:    
        With = [key for key, value in RSquared.items() if str(i) in str(key)]
        Rsq_with = [value for key, value in RSquared.items() if str(i) in str(key)]
        Without =[sub.replace(str(i), '') for sub in With] 
        Rsq_without = [RSquared[x] for x in  Without]
        df = pd.DataFrame(list(zip(With, Rsq_with,Without,Rsq_without)),columns=['With','Rsq_with','Without','Rsq_without'])
        df['Diff'] = df['Rsq_with'] - df['Rsq_without'] 
        df['Weights'] = (df['Without'].str.len().apply(abs).apply(math.factorial) * (n- (df['Without'].str.len().apply(abs))-1).apply(math.factorial))/math.factorial(n)
        df['Weights_Diff'] = df['Diff']*df['Weights']
        Shapely_dict[i]= sum(df['Weights_Diff'])
    return Shapely_dict

    

    
    



