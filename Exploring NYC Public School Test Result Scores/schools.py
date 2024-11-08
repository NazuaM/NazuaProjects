import pandas as pd

# Read in the data
schools = pd.read_csv('schools.csv')

# Preview the data
schools.head()

# Which NYC schools have the best math results?
best_math_schools = schools[schools['average_math'] >= 640][['school_name', 'average_math']].sort_values('average_math', ascending=False).reset_index(drop=True)
print(best_math_schools)

# What are the top 10 performing schools based on the combined SAT scores?
best_math_schools["total_SAT"] = schools['average_reading'] + schools['average_writing'] + schools['average_math']
top_10_schools = best_math_schools.drop(columns = 'average_math').sort_values('total_SAT', ascending = False).iloc[:10].reset_index(drop=True)
print(top_10_schools)

# Which single borough has the largest standard deviation in the combined SAT score?
schools["total_SAT"] = schools['average_reading'] + schools['average_writing'] + schools['average_math']

largest_std_dev = schools.pivot_table(values='total_SAT', index='borough', aggfunc=['mean', 'std']).round(2)

condition = largest_std_dev[('std','total_SAT')]
largest_std_dev = largest_std_dev[condition == condition.max()]

countt = schools.groupby('borough')['school_name'].count()

largest_std_dev["num_schools"] = countt.loc[largest_std_dev.index]

largest_std_dev.columns = ["average_SAT", "std_SAT", "num_schools" ]

largest_std_dev = largest_std_dev[['num_schools', 'average_SAT', 'std_SAT']]

print(largest_std_dev)