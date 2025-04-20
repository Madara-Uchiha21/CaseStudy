#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_csv("C:\\Users\\rajpr\\OneDrive\\Desktop\\CODING\\DataScience\\CaseStudies\\US_honey_dataset.csv")
df.head()

# %%
df.info()
df.describe()

# %%
print(df.isnull().sum())
print()

# %%
df.head(20)
print()

# %%
df.drop(["Unnamed: 0"], axis=1, inplace=True)   # Drop the index column
df.head(20)
print()

# %%
# nunique() - number of unique values in each column
# unique()  -  unique values in each column
# value_counts() - count of unique values in each column

print("nUnique value in each column")
df["state"].nunique()

#%%
print("Unique value in each column")
df["state"].unique()

#%%
print("Value counts in each column")
df["state"].value_counts()
print()

# %%
print("describe function for non-numeric values")
df.describe(include="object")
print()

# %%
print("type of each column")
df.dtypes

#%%
print("Dropping something Permanentaly")
df = df.drop((["Unnamed: 0"]), axis=1) 

# %%
# Printing after dropping Unnamed
df
# %%
# Finding Duplicate dataset
df.duplicated().sum()

# %%
"""Q1. Which state are rarely contributing to honey production
for last 27 years?, Visulaize the data by pie chart."""
# ANSWER :
df.head(20)
# %%
data = df["state"].value_counts()
data
# %%
# Pie chart:
plt.figure(figsize=(15,15))
plt.pie(data.values, labels=data.index,autopct="%0.2f%%")
plt.title("Honey Production by State for last 27 years")
plt.show()

""" Here,
* figsize is to increase the size
* data.values - to get the values of the data
* labels=data.index - to get the index of the data
/Name in the piechart
* autopct="%0.2f%%" - to get the percentage of each state in the piechart"""

# %%
"""Q2. Which are the top 5 states contributing to honey production in US?"""
# ANSWER:
""" Top = df["production"].nlargest(5)
print(Top) """
# First we need to find the sum of production, as there is
# Mention of state for multiple time.
Net_Production = df.groupby("state")["production"].sum().reset_index()
Net_Production
# %%
# Now I have to arrange it in descending order
Net_Production = Net_Production.sort_values(by="production",ascending=False)
Net_Production.head(5)
# %%
# Now representing it in Graph
plt.figure(figsize=(15,15))
sns.barplot(Net_Production, x = "state", y ="production",color="Red")
plt.title("Most to least Honey Produucing States")
plt.xlabel("States")
plt.ylabel("Production")
plt.show()

# %%
""" Q3. Which was the year when production 
of Honey in US was the Heighest?"""
# ANSWER:
Highest_Production = df.groupby("year")["production"].sum().reset_index()
Highest_Production
# %%
plt.figure(figsize=(15,15))
plt.xlabel("Year")
plt.ylabel("Production")
sns.barplot(x="year", y="production", data=Highest_Production, color="Green")
plt.title("Honey Production in US by Year")
# %%
# Top 5 years with highest production
Highest_Production.head(5)

# %%
# Now creatinh bar graph of top 5 years 
Top_5 = Highest_Production.head(5)
sns.barplot(x="year", y="production", data=Top_5, color="Black")
plt.title("Top 5 Years with Highest Production")
plt.xlabel("Year")
plt.ylabel("Production")
plt.show()
# %%
"""
plt.violinplot(Top_5["production"])
plt.show() """

# %%
""" Q4. Which state has heighest number of colonies in year 2000?"""
# ANSWER:
# First we need to look after data
df.head(10)
# %%
# First we need to filter the data for yeaar 2000
Year_2000 = df[df["year"]==2000]
Year_2000
# %%
# Now we have to check is there any null or duplicate value 
# Checking Null values
Nv=Year_2000.isnull().sum()
Dv = Year_2000.duplicated().sum()
print(f"Null values in Year 2000: {Nv} and Duplicate values in Year 2000: {Dv}")

# %%
# Now sort the data acc to colonies
Year_2000 = Year_2000.sort_values(by="colonies_number", ascending = False)
Year_2000.head(5)

# %%
# Now create some bar graph for the data
plt.figure(figsize=(15,15))
sns.barplot(x="state", y="colonies_number", data=Year_2000, color=(85/255, 107/255, 47/255))
plt.title("States with Highest Number of Colonies in Year 2000")
plt.xlabel("States")
plt.ylabel("Colonies Number")

plt.show()

# %%
