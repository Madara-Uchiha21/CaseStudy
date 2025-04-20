#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# %%
df = pd.read_csv("C:\\Users\\rajpr\\OneDrive\\Desktop\\CODING\\DataScience\\CaseStudies\\CaseStudy2\\people (1).csv")
df

# %%
df.describe()

# %%
df.info()

# %%
df.isnull().sum()

# %%
df.duplicated()

#%%
df.duplicated().sum()

# %%
# Drop Duplicated Rows
df.drop_duplicates(inplace=True)  

# %%
df.duplicated().sum()

# %%
df

# %%
# nunique() , unique() , value_counts()  are  the function of pandas
df["salary"].nunique()

# %%
df["salary"].value_counts()

# %%
df["salary"].unique()

# %%
print("Talks about Shape of the DataFrame.")
df.shape

# %%
#Hue is used to add another dimension to the plot, allowing us to visualize the relationship between three variables at once.
# Ques1. Does number of projects effect employee leaving company?
# Also write suggestion for the same.

plt.figure(figsize=(10, 6))
sns.countplot(data = df, x = "numberOfProjects", hue = "left")
plt.title("Number of Projects vs Employee Leaving")
plt.show()


# %%
# Doubt************
plt.figure(figsize=(10, 6))

# Create the count plot
ax = sns.countplot(data=df, x="numberOfProjects", hue="left")

# Calculate the counts for each bar
counts = df.groupby(["numberOfProjects", "left"]).size().unstack(fill_value=0)
#
# Get the x-tick positions
x_positions = range(len(counts.index))

# Plot the blue line (for left=0)
plt.plot(x_positions, counts[0], color="blue", marker="o", label="Left=0")

# Plot the orange line (for left=1)
plt.plot(x_positions, counts[1], color="orange", marker="o", label="Left=1")

# Add title, labels, and legend
plt.title("Number of Projects vs Employee Leaving")
plt.xlabel("Number of Projects")
plt.ylabel("Count")
plt.legend(title="Employee Left")

# Adjust x-ticks to match the bar positions
plt.xticks(ticks=x_positions, labels=counts.index)

plt.show()
print()

# %%
# Gettin the data in numbers on top of bars
plt.figure(figsize=(10, 6))

# Create the count plot
ax = sns.countplot(data=df, x="numberOfProjects", hue="left")

# Annotate the bars with the actual counts
for container in ax.containers:
    ax.bar_label(container, fmt='%d', label_type='edge')  # Display integer values on top of bars

# Add title and labels
plt.title("Number of Projects vs Employee Leaving")
plt.xlabel("Number of Projects")
plt.ylabel("Count")

plt.show()
# %%
df[df["numberOfProjects"]==3]
print()

# %%
# Ques2. Does timeSpent.company effect employee leaving company?
plt.figure(figsize=(10, 6))
ax1 = sns.countplot(data=df,x="timeSpent.company",hue="left")

# Annotation the bars with numerical values
for container in ax1.containers:
    ax1.bar_label(container,fmt='%d',label_type='edge')

# Add titles to the plot
plt.title("Time spent in company vs Employee Leaving")
plt.xlabel("Time spent in Comapny")
plt.ylabel("Count")
plt.legend(title="TimeSpent vs Employee Left")
plt.show()

# %%
# Ques3. Dept vs left % walla
plt.figure(figsize=(10,6))
new = sns.countplot(data=df,x="dept",hue="left")

# Annotation the bars with numerical values
for container in new.containers:
    new.bar_label(container,fmt='%d',label_type='edge')

# title
plt.title("Dept vs leaving Emp")
plt.xlabel("Dept")
plt.ylabel("Count")
plt.legend(title="Dept vs Emp Left")
plt.xticks(rotation=90)
plt.show()

#%%
# Ques3. Dept vs left
plt.figure(figsize=(10, 6))
new = sns.countplot(data=df, x="dept", hue="left")

# Calculate total counts for each group
total_counts = df.groupby("dept").size()

# Annotate the bars with percentages
for container in new.containers:
    for bar in container:
        height = bar.get_height()  # Get the height of the bar (count)
        if height > 0:  # Avoid division by zero
            dept = bar.get_x() + bar.get_width() / 2  # Get the x-position of the bar
            total = total_counts.iloc[int(dept)]  # Get the total count for the department
            percentage = (height / total) * 100  # Calculate percentage
            new.text(bar.get_x() + bar.get_width() / 2, height, f'{percentage:.1f}%', ha='center', va='bottom')

# Title and labels
plt.title("Dept vs Leaving Emp (with Percentages)")
plt.xlabel("Dept")
plt.ylabel("Count")
plt.legend(title="Dept vs Emp Left")
plt.xticks(rotation=90)
plt.show()

# %%
# Ques4. Dept vs salary
print("Dept vs Salary")
plt.figure(figsize=(10, 6))
chk = sns.countplot(data=df,x='dept',hue='salary')

# Annotation
for container in chk.containers:
    chk.bar_label(container,fmt='%d',label_type='edge')

plt.title("Dept vs Salary")
plt.xlabel("Dept")
plt.ylabel("Count")
plt.legend(title="Dept vs Salary")
plt.xticks(rotation=90)
plt.show()
print()

# %%
# Ques5. How does work accident effect employee leaving company?
print("Work Accident vs Employee Leaving")
df.value_counts('workAccident')

plt.figure(figsize=(10,6))
wa = sns.countplot(data=df,x="workAccident",hue="left")

for container in wa.containers:
    wa.bar_label(container,fmt='%d',label_type='edge')

plt.title("Work Accident vs Employee Leaving")
plt.xlabel("Work Accident")
plt.ylabel("Count")
plt.xtricks(rotation=50)
plt.legend(title="Acc vs Left")
plt.show()
