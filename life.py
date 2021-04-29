import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#from scipy import stats

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
life = pd.read_csv('/home/sveta/PycharmProjects/life_expectancy/all_data.csv')



life.rename(columns = {'Life expectancy at birth (years)' : 'expectancy'}, inplace=True)
life.rename(columns = {'Country' : 'country'}, inplace=True)
life.rename(columns= {'GDP': 'gdp'}, inplace=True)

life_exp = life.expectancy
print(life.head())
print(life.info())


average_life_exp = np.mean(life_exp)
median_life_exp = np.median(life_exp)

#Mode. The most frequently occurring observation in the dataset
array_life_exp = np.array(life_exp)
#mode_life_exp = stats.mode(array_life_exp)
#print("Mode Life Expectancy {0}".format(mode_life_exp))

minimum_life_exp = life_exp.min()
maximum_life_exp = life_exp.max()
print("Average Life Expectancy {0}, Minimum Life Expectancy {1}, Maximum Life Expectancy {2}".format(average_life_exp, minimum_life_exp, maximum_life_exp))

plt.hist(life_exp, edgecolor='black')
plt.title('Life Expectancy at birth (years)')
plt.xlabel('Life Expectancy')
plt.ylabel('Count')
plt.axvline(average_life_exp, color='r', linestyle='solid', linewidth=2, label="Mean")
plt.axvline(median_life_exp, color='y', linestyle='dotted', linewidth=2, label="Median")
plt.legend()
#plt.show()

#it's interesting to build the plot for each country
print(life.country.unique())

chile_life_exp = life.expectancy[life.country == 'Chile']
china_life_exp = life.expectancy[life.country == 'China']
germany_life_exp = life.expectancy[life.country == 'Germany']
mexico_life_exp = life.expectancy[life.country == 'Mexico']
usa_life_exp = life.expectancy[life.country == 'United States of America']
zimbabwe_life_exp = life.expectancy[life.country == 'Zimbabwe']

plt.boxplot([chile_life_exp, china_life_exp, germany_life_exp, mexico_life_exp, usa_life_exp, zimbabwe_life_exp], labels=['Chile', 'China', 'Germany', 'Mexico', 'USA', 'Zimbabwe'])
#plt.show()

#Associations: two quantative variables - expectancy and GDP
#scatter plot
plt.scatter(x=life.expectancy, y=life.gdp)
plt.xlabel('Life Expectancy at birth (years')
plt.ylabel('GDP')
#plt.show()
#A large negative covariance indicates a strong negative linear association where large values of one variable are associated with small values of the other.
# A large positive covariance indicates a strong positive linear association where large values of one variable are associated with large values of the other.
# A covariance of 0 indicates there is no linear relationship.
cov_mat_exp_gdp = np.cov(life.expectancy, life.gdp)
print(cov_mat_exp_gdp)

#from scipy.stats import pearsonr
#corr_exp_gdp, p = pearsonr(life.expectancy, life.gdp)
#print(corr_exp_gdp)