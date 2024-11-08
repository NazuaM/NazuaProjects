import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load and clean data
df = pd.read_csv('netflix_data.csv')
df_cleaned = df.dropna()
df_new = df_cleaned.assign(genre=df_cleaned['genres'].str.split(',')).explode('genre').drop(columns=['genres'])

#Change in Genre Proportion (2015-2020 vs 2010-2015)

# Filter data for the two periods
df_2010 = df_new[np.logical_and(df_new['releaseYear'] >= 2010, df_new['releaseYear'] < 2015)]
df_2015 = df_new[np.logical_and(df_new['releaseYear'] >= 2015, df_new['releaseYear'] < 2020)]

# Get normalized genre counts (proportions) for each period
df_2010_genre = df_2010['genre'].value_counts(normalize=True)
df_2015_genre = df_2015['genre'].value_counts(normalize=True)

# Align genres across both periods
all_genres = sorted(set(df_2010_genre.index).union(set(df_2015_genre.index)))
df_2010_genre = df_2010_genre.reindex(all_genres, fill_value=0)
df_2015_genre = df_2015_genre.reindex(all_genres, fill_value=0)

# Calculate the difference in proportions between 2015-2020 and 2010-2015
genre_difference = df_2015_genre - df_2010_genre
genre_difference = genre_difference[genre_difference.abs() >= 0.002]

# Plot the difference
plt.figure(figsize=(12, 6))
plt.bar(genre_difference.index, genre_difference.values, color='blue', alpha=0.7)

# Add titles and labels
plt.title('Change in Genre Proportion (2015-2020 vs 2010-2015)')
plt.xlabel('Genre')
plt.ylabel('Change in Proportion')
plt.xticks(rotation=45)
plt.axhline(0, color='black', linewidth=0.5)  # Reference line at 0
plt.tight_layout()

# Show plot
plt.show()

plt.clf()

#How many movies were released each year?
released_per_year = df_cleaned['releaseYear'].value_counts().sort_index()
plt.figure(figsize=(10, 5))
plt.plot(released_per_year.index, released_per_year.values, marker = 'x')
plt.title('How many movies were released each year?')
plt.xlabel('Year')
plt.ylabel('Number of movies')
plt.tight_layout()

# Show plot
plt.show()

plt.clf()

#What is the distribution of IMDb ratings?
mininum_votes = 50000
IMDb = df_cleaned[df_cleaned['imdbNumVotes'] >= mininum_votes]
plt.figure(figsize=(10,5))
plt.hist(IMDb['imdbAverageRating'], bins = 10, color='skyblue', edgecolor='black')
plt.title('Distribution of IMDb Ratings (Minimum Votes: 50,000)')
plt.xlabel('IMDb Rating')
plt.ylabel('Frequency')
plt.xticks(np.arange(0,10.5,0.5))
plt.grid(axis='y', alpha=0.75)
plt.show()

plt.clf()
#Find the top-rated movies.
top_rated_movies = IMDb[IMDb['imdbAverageRating'] >= 9]
plt.figure(figsize=(10, 5))
top_rated_movies_genre = top_rated_movies['releaseYear'].value_counts().sort_index()
plt.bar(top_rated_movies_genre.index, top_rated_movies_genre.values, color='blue', alpha=0.7)

# Add titles and labels
plt.title('Release Year Distribution of Top-Rated Movies (IMDb Rating >= 9)')
plt.xlabel('Release Year')
plt.ylabel('Number of Top-Rated Movies')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


