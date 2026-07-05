# Load necessary libraries
library(ggplot2)
library(dplyr)

# Load the data set
netflix_data <- read.csv("Netflix_shows_movies.csv")

# Data Exploration
head(netflix_data)

# Data Cleaning
netflix_data <- netflix_data %>%
  mutate(
    director = ifelse(is.na(director), "Unknown", director),
    cast = ifelse(is.na(cast), "Unknown", cast),
    country = ifelse(is.na(country), "Unknown", country),
    rating = ifelse(is.na(rating), "Not Rated", rating),
    date_added = ifelse(is.na(date_added), "Unknown", date_added)
  )

# Step 4: Data Visualization - Ratings Distribution
ggplot(data = netflix_data, aes(x = rating)) +
  geom_bar(stat = "count", fill = "steelblue") +
  theme_minimal() +
  labs(title = "Ratings Distribution", x = "Rating", y = "Count") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

