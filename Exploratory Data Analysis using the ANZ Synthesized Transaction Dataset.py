#!/usr/bin/env python
# coding: utf-8

# ## Business Understanding

# Task 1: Segment the dataset and draw unique insights, including visualisation of the transaction volume and assessing the effect of any outliers.

# #  The Dataset
# The synthesised transaction dataset contains 3 months’ worth of transactions for 100 hypothetical customers. It contains purchases, recurring transactions, and salary transactions.
# 
# The dataset is designed to simulate realistic transaction behaviours that are observed in ANZ’s real transaction data, so many of the insights you can gather from the tasks below will be genuine.

# ## Importing the required libraries

# In[50]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ## Reading the Dataset

# In[5]:


ANZ = pd.read_excel(r"C:\Users\seyi\Downloads\ANZ synthesised transaction dataset.xlsx")


# In[6]:


ANZ.head()


# In[7]:


ANZ.info()


# In[8]:


ANZ.shape


# In the ANZ dataset, there are 23 different columns and 12043 observations

# In[9]:


ANZ.columns


# In[10]:


ANZ.describe()


# To confirm that we are dealing with 100 hypothetical customers:

# In[11]:


ANZ['account'].nunique()


# ## Taking the relevant features

# In[12]:


ANZ = ANZ[["status","card_present_flag","balance","date",
                   "gender","age","merchant_suburb","merchant_state",
                   "amount","customer_id","movement"]]
ANZ["date"] = pd.to_datetime(ANZ["date"])
ANZ.head()


# In[13]:


Null_values = ANZ.isnull().sum().sort_values(ascending=False)


# In[14]:


Null_values


# ## Exploratory Data Analysis (including Visualizations)

# ### Total number of autorized and posted status

# In[15]:


ANZ['status'].value_counts()


# ### Total number of transactions made on each day

# In[16]:


ANZ['date'].value_counts()


# ### Total number of transactions made by each customer

# In[17]:


ANZ['customer_id'].value_counts()


# ### Transaction volume made by customers each day

# In[18]:


ANZ_date_count = ANZ.groupby('date').count()


# In[19]:


transaction_volume = ANZ_date_count['customer_id'].mean()


# In[20]:


length = len(ANZ_date_count.index)


# In[21]:


plt.figure()
plt.plot(ANZ_date_count.index, ANZ_date_count["customer_id"], c="blue", label = "Customer ID")
plt.plot(ANZ_date_count.index, np.linspace(transaction_volume,transaction_volume,length), c="g", label = "mean transaction volume")
plt.title("ANZ Transaction Volume vs. Date")
plt.xlabel("Date")
plt.ylabel("Number of customers")
plt.legend()
plt.tight_layout()


# ## What is the average transaction amount?

# In[22]:


ANZ_date_mean = ANZ.groupby('date').mean()


# In[23]:


transaction_amount = ANZ_date_count['amount'].mean()


# In[24]:


length = len(ANZ_date_count.index)


# In[25]:


plt.figure()
plt.plot(ANZ_date_count.index, ANZ_date_mean["amount"], c="red", label = "Amount")
plt.plot(ANZ_date_count.index, np.linspace(transaction_amount,transaction_amount,length), c="b", label = "Overall mean transaction amount")
plt.title("ANZ mean Transaction Amount vs. Date")
plt.xlabel("Date")
plt.ylabel("Amount ($)")
plt.legend()
plt.tight_layout()


# ## What is the average customer balance and payment amount by Age

# In[26]:


months = []
for date in ANZ["date"]:
    if date.month == 8:
        months.append("August")
    elif date.month == 9:
        months.append("September")
    elif date.month == 10:
        months.append("October")

ANZ["Months"] = months
ANZ["Months"].head()


# ### For August:

# In[27]:


ANZ_cus_aug = ANZ[ANZ["Months"] == "August"].groupby("customer_id").mean()


# In[28]:


ANZ_gen_aug = ANZ[ANZ["Months"] == "August"].groupby("gender").mean()


# In[29]:


mean_f_bal_aug = ANZ_gen_aug["balance"].iloc[0]
mean_m_bal_aug = ANZ_gen_aug["balance"].iloc[1]
length = len(ANZ_cus_aug["age"])


# In[47]:


plt.figure()
plt.scatter(ANZ_cus_aug["age"], ANZ_cus_aug["balance"], c="red", label="Balance")
plt.plot(ANZ_cus_aug["age"], np.linspace(mean_f_bal_aug,mean_f_bal_aug,length), c="g", label = "mean female balance")
plt.plot(ANZ_cus_aug["age"], np.linspace(mean_m_bal_aug,mean_m_bal_aug,length), c="b", label = "mean male balance")
plt.title("ANZ Average Customer Balance vs. Age for August")
plt.xlabel("Age (years)")
plt.ylabel("Balance ($)")
plt.legend()
plt.tight_layout()


# In[31]:


mean_f_amt_aug = ANZ_gen_aug["amount"].iloc[0]
mean_m_amt_aug = ANZ_gen_aug["amount"].iloc[1]


# In[48]:


plt.scatter(ANZ_cus_aug["age"], ANZ_cus_aug["amount"], c="orange", label="Amount")
plt.plot(ANZ_cus_aug["age"], np.linspace(mean_f_amt_aug,mean_f_amt_aug,length), c="r", label = "mean female amount")
plt.plot(ANZ_cus_aug["age"], np.linspace(mean_m_amt_aug,mean_m_amt_aug,length), c="b", label = "mean male amount")
plt.title("ANZ Customer Average Payment Amount vs. Age for August")
plt.xlabel("Age (years)")
plt.ylabel("Amount ($)")
plt.legend()
plt.tight_layout()


# ### For September:

# In[33]:


ANZ_cus_sep = ANZ[ANZ["Months"] == "September"].groupby("customer_id").mean()
ANZ_gen_sep = ANZ[ANZ["Months"] == "September"].groupby("gender").mean()


# In[34]:


mean_f_bal_sep = ANZ_gen_sep["balance"].iloc[0]
mean_m_bal_sep = ANZ_gen_sep["balance"].iloc[1]
length = len(ANZ_cus_sep["age"])


# In[49]:


plt.figure()
plt.scatter(ANZ_cus_sep["age"], ANZ_cus_sep["balance"], c="grey", label="Balance")
plt.plot(ANZ_cus_sep["age"], np.linspace(mean_f_bal_sep,mean_f_bal_sep,length), c="r", label = "mean female balance")
plt.plot(ANZ_cus_sep["age"], np.linspace(mean_m_bal_sep,mean_m_bal_sep,length), c="b", label = "mean male balance")
plt.title("ANZ Customer Balance vs. Age for September")
plt.xlabel("Age (years)")
plt.ylabel("Balance ($)")
plt.legend()
plt.tight_layout()


# In[36]:


mean_f_amt_sep = ANZ_gen_sep["amount"].iloc[0]
mean_m_amt_sep = ANZ_gen_sep["amount"].iloc[1]


# In[37]:


plt.scatter(ANZ_cus_sep["age"], ANZ_cus_sep["amount"], c="green", label="Amount")
plt.plot(ANZ_cus_sep["age"], np.linspace(mean_f_amt_sep,mean_f_amt_sep,length), c="r", label = "mean female amount")
plt.plot(ANZ_cus_sep["age"], np.linspace(mean_m_amt_sep,mean_m_amt_sep,length), c="b", label = "mean male amount")
plt.title("ANZ Customer mean Payment Amount vs. Age for September")
plt.xlabel("Age (years)")
plt.ylabel("Amount ($)")
plt.legend()
plt.tight_layout()


# ### For October:

# In[38]:


ANZ_cus_oct = ANZ[ANZ["Months"] == "October"].groupby("customer_id").mean()
ANZ_gen_oct = ANZ[ANZ["Months"] == "October"].groupby("gender").mean()


# In[39]:


mean_f_bal_oct = ANZ_gen_oct["balance"].iloc[0]
mean_m_bal_oct = ANZ_gen_oct["balance"].iloc[1]
length = len(ANZ_cus_oct["age"])


# In[40]:


plt.figure()
plt.scatter(ANZ_cus_oct["age"], ANZ_cus_oct["balance"], c="black", label="Balance")
plt.plot(ANZ_cus_oct["age"], np.linspace(mean_f_bal_oct,mean_f_bal_oct,length), c="r", label = "mean female balance")
plt.plot(ANZ_cus_oct["age"], np.linspace(mean_m_bal_oct,mean_m_bal_oct,length), c="b", label = "mean male balance")
plt.title("ANZ Customer Balance vs. Age for October")
plt.xlabel("Age (years)")
plt.ylabel("Balance ($)")
plt.legend()
plt.tight_layout()


# In[41]:


mean_f_amt_oct = ANZ_gen_oct["amount"].iloc[0]
mean_m_amt_oct = ANZ_gen_oct["amount"].iloc[1]


# In[42]:


plt.scatter(ANZ_cus_oct["age"], ANZ_cus_oct["amount"], c="purple", label="Amount")
plt.plot(ANZ_cus_oct["age"], np.linspace(mean_f_amt_oct,mean_f_amt_oct,length), c="r", label = "mean female amount")
plt.plot(ANZ_cus_oct["age"], np.linspace(mean_m_amt_oct,mean_m_amt_oct,length), c="b", label = "mean male amount")
plt.title("ANZ Customer mean Payment Amount vs. Age for October")
plt.xlabel("Age (years)")
plt.ylabel("Amount ($)")
plt.legend()
plt.tight_layout()


# Using an heatmap: 

# In[46]:


corrmat = ANZ.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True);


# In[ ]:




