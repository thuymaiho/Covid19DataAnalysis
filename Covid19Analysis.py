
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Import the dataset
dataset_corona = pd.read_csv(r'D:\Data Analysis\covid19_Confirmed_dataset.csv')
dataset_corona.head()

#Check the dataset shape
dataset_corona.shape

#Delete the useless columns
df= dataset_corona.drop(["Lat", "Long"], axis=1, inplace=True)
dataset_corona.head(10)

#Aggregating the rows by the country
dataset_aggregated = dataset_corona.groupby("Country/Region").sum()
dataset_aggregated.head()
dataset_aggregated.shape

#Visualizing data related to countries.
dataset_aggregated.loc["China"].plot()
dataset_aggregated.loc["Italy"].plot()
dataset_aggregated.loc["Spain"].plot()
plt.legend()

#Calculating a good measure
dataset_aggregated.loc["China"][:3].plot()
#Plotting the first derivative of the curve
dataset_aggregated.loc["China"].diff().plot()
#Find the maximum infection rate for China, Italy, Netherlands
dataset_aggregated.loc["China"].diff().max()
dataset_aggregated.loc["Italy"].diff().max()
dataset_aggregated.loc["Netherlands"].diff().max()

#Find the maximum infection rate for all of the countries
countries = list(dataset_aggregated.index)
max_infection_rates = []
for c in countries:
    max_infection_rates.append(dataset_aggregated.loc[c].diff().max())
dataset_aggregated["max_infection_rates"] = max_infection_rates
dataset_aggregated.head()

#Create a new dataframe with only needed column
corona_data = pd.DataFrame(dataset_aggregated["max_infection_rates"])
corona_data.head()
corona_data.shape

report_csv = pd.read_csv(r'D:\Data Analysis\worldwide_happiness_report.csv')
report_csv.head()
#Drop the useless columns
uselessCols = ["Overall rank", "Score", "Generosity", "Perceptions of corruption"]
report_csv.drop(uselessCols, axis=1, inplace=True)
#Change the indices of the dataframe
report_csv.set_index("Country or region", inplace=True)
report_csv.head()
report_csv.shape
#Join the two datasets
data = corona_data.join(report_csv, how="inner")
data.head()
#Correlation matrix
data.corr()
#Plotting GDP vs maximum Infection rate
x = data["GDP per capita"]
y = data["max_infection_rates"]
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))
