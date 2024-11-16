# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Question 1: Global peak search for 'workout'
workout = pd.read_csv("Market Analysis\Data\workout.csv")
peak = workout.loc[workout['workout_worldwide'] == workout['workout_worldwide'].max(), 'month']
year_str = str(pd.to_datetime(peak.iloc[0]).year)

# Question 2: Most popular keyword during the COVID period and currently
three_key = pd.read_csv(r"Market Analysis\Data\three_keywords.csv")

# Define the time periods for peak interest during COVID and current interest
covid_condition = (three_key['month'] >= '2020-03') & (three_key['month'] <= '2022-01')
peak_covid_period = three_key[covid_condition]
peak_covid_agg = peak_covid_period.agg({'home_workout_worldwide': 'mean', 'gym_workout_worldwide': 'mean', 'home_gym_worldwide': 'mean'})
peak_covid = peak_covid_agg.idxmax()

# Define current interest period
current_condition = (three_key['month'] >= '2022-01')
current_period = three_key[current_condition]
current_agg = current_period.agg({'home_workout_worldwide': 'mean', 'gym_workout_worldwide': 'mean', 'home_gym_worldwide': 'mean'})
current = current_agg.idxmax()

# Question 3: Country with the highest interest in 'workout'
three_country = pd.read_csv("Market Analysis\Data\workout_geo.csv")
country = three_country[three_country['country'].isin(['United States', 'Australia', 'Japan'])]
top_country = country.loc[country['workout_2018_2023'] == country['workout_2018_2023'].max(), 'country'].iloc[0]

# Question 4: Country with the highest interest in 'home workout' between Philippines and Malaysia
four_country = pd.read_csv(r"Market Analysis\Data\three_keywords_geo.csv")
three_geo = four_country[four_country['Country'].isin(['Philippines', 'Malaysia'])]
home_workout_geo = three_geo.loc[three_geo['home_workout_2018_2023'] == three_geo['home_workout_2018_2023'].max(), 'Country'].iloc[0]

print(year_str, peak_covid, current, top_country, home_workout_geo)