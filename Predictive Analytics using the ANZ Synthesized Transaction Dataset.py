#!/usr/bin/env python
# coding: utf-8

# ## Business Understanding

# Task 2: Explore correlations between customer attributes, build a regression and a decision-tree prediction model based on your findings.

# In[9]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor


# In[2]:


data = pd.read_excel(r"C:\Users\seyi\Downloads\ANZ synthesised transaction dataset.xlsx")


# In[3]:


data.head(3)


# In[4]:


data_salaries = data[data['txn_description']=='PAY/SALARY'].groupby('customer_id').mean()


# In[5]:


data_salaries.head()


# In[6]:


salaries = []
for customer_id in data['customer_id']:
    salaries.append(int(data_salaries.loc[customer_id]['amount']))
    
data['annual_salary'] = salaries


# In[7]:


data_cust = data.groupby("customer_id").mean()
data_cust.head()


# In[10]:


corrmat = data.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True);


# In[29]:


import matplotlib.pyplot as plt

age_cust = data['age']
salary = data['annual_salary']

plt.scatter(age_in, salary)
plt.title('Age vs. Annual_Salary')
plt.xlabel('Age')
plt.ylabel('Annual_Salary')
plt.show()


# ## Predictive Analysis

# #### Building a simple regression model:

# In[11]:


N_train = int(len(data_cust)*0.8)
X_train = data_cust.drop("annual_salary", axis=1).iloc[:N_train]
Y_train = data_cust["annual_salary"].iloc[:N_train]
X_test = data_cust.drop("annual_salary", axis=1).iloc[N_train:]
Y_test = data_cust["annual_salary"].iloc[N_train:]


# In[12]:


lin_reg = LinearRegression()

lin_reg.fit(X_train, Y_train)
lin_reg.score(X_train, Y_train)


# In[13]:


lin_reg.predict(X_test)


# In[14]:


lin_reg.score(X_test, Y_test)


# #### The challenge: Building a decision-tree based model

# In[15]:


data_cat = data[["txn_description", "gender", "age", "merchant_state", "movement"]]


# In[16]:


pd.get_dummies(data_cat).head()


# In[17]:


N_train = int(len(data)*0.8)
X_train = pd.get_dummies(data_cat).iloc[:N_train]
Y_train = data["annual_salary"].iloc[:N_train]
X_test = pd.get_dummies(data_cat).iloc[N_train:]
Y_test = data["annual_salary"].iloc[N_train:]


# #### For Classification (Using the DecisionTreeClassifier)

# In[18]:


decision_tree_class = DecisionTreeClassifier()


# In[19]:


decision_tree_class.fit(X_train, Y_train)
decision_tree_class.score(X_train, Y_train)


# In[20]:


decision_tree_class.predict(X_test)


# In[21]:


decision_tree_class.score(X_test, Y_test)


# #### For Regression (Using the DecisionTreeRegressor)

# In[22]:


decision_tree_reg = DecisionTreeRegressor()


# In[23]:


decision_tree_reg.fit(X_train, Y_train)
decision_tree_reg.score(X_train, Y_train)


# In[24]:


decision_tree_reg.predict(X_test)


# In[25]:


decision_tree_reg.score(X_test, Y_test)

