# TASK 1 - Abalone Dataset Analysis

## Overview

The task in this assignment is to perform a statistical analysis of the given dataset, using Jupyter Notebook.

The data to be analyzed concerns snails called abalones. The dataset comprises 9 variables (attributes, features) of these snails and contains 4177 observations. One of the variables is qualitative (sex), whereas the others are quantitative.

The analysis will be performed using Jupyter Notebook and documented as a Jupyter notebook.

## Requirements

1. **Table of Distribution for Qualitative Variable**:
   - Create a table of the distribution of the qualitative variable in the dataset.
   - Structure:
     - Rows: individual categories
     - Columns: category name, count, percentage (rounded to two decimal places)

2. **Summary Statistics Table for Quantitative Variables**:
   - Create a table with summary statistics for the quantitative variables in the dataset.
   - Structure:
     - Rows: individual variables
     - Columns: variable name, arithmetic mean, standard deviation, minimum value, 1st quartile, 2nd quartile (median), 3rd quartile, maximum value

3. **Bar Chart for Qualitative Variable**:
   - Create a bar chart of the counts of occurrences of each category for the qualitative variable in the dataset.

4. **Histograms for Quantitative Variables**:
   - Create a histogram of each quantitative variable in the dataset. All histograms should be placed in a single figure spanning 4 rows and 2 columns.

5. **Scatter Plots for Quantitative Variables**:
   - Create a scatter plot for each pair of the quantitative variables in the dataset. All scatter plots should be placed in a single figure spanning 14 rows and 2 columns.

6. **Correlation Matrix Table**:
   - Create a table representing a linear correlation matrix of all quantitative variables in the dataset.

7. **Heatmap for Correlation Matrix**:
   - Create a heatmap representing a linear correlation matrix of all quantitative variables in the dataset.

8. **Linear Regression Plot**:
   - Create a linear regression plot with the two quantitative variables that are most strongly linearly correlated.


9. **Summary Statistics Table Split by Qualitative Variable**:
   - Create a table with summary statistics for the quantitative variables in the dataset split by the categories of the qualitative variable.
   - Structure:
     - Rows: combinations of individual quantitative variables and individual categories of the qualitative variable
     - Columns: quantitative variable name, qualitative variable category name, arithmetic mean, standard deviation, minimum value, 1st quartile, 2nd quartile (median), 3rd quartile, maximum value

10. **Boxplot for Quantitative Variables Grouped by Qualitative Variable**:
   - Create a boxplot of each quantitative variable in the dataset, grouping every one of them by the qualitative variable. All boxplots should be placed in a single figure spanning 4 rows and 2 columns.



# TASK 2 - Simulation: Wolf and Sheep in a Meadow

## Overview

The task in this assignment is to develop a simulation involving a wolf that tries to catch sheep scattered in a meadow, which uses text mode.

The simulation involves two animal species: a single wolf and a herd of sheep. These animals move around an infinite meadow with no terrain obstacles: the wolf chases the sheep, trying to catch them and then eat them, while the sheep try (rather clumsily) to escape from the wolf. According to these stipulations, the meadow is represented as an infinite two-dimensional space with the center located at the point (0.0; 0.0), thus using a Cartesian coordinate system, whereas the position of each animal in the meadow is defined as a pair of floating-point numbers (the coordinates can take on both positive and negative values).

At the beginning of the simulation, the initial positions of all animals are determined. The initial position of each sheep is chosen randomly, with each coordinate being drawn from a range that extends symmetrically around 0 over positive and negative numbers, and where chosen values are floating-point numbers, which need not be whole. Given that the range is symmetrical around 0, its specification is governed by a single predefined value that is the absolute value of the limit imposed on the coordinates (hence the range spans from the negative of this value to this value). The initial position of the wolf is the center of the meadow, that is the point (0.0; 0.0).

The simulation is advanced in rounds. In the first stage of every round, all alive sheep move one by one, and afterwards, in the second stage, the wolf moves. During its movement, a sheep first randomly chooses one of the four directions: north (up), south (down), east (right), or west (left), and then moves a predefined distance in the chosen direction. In turn, the wolf first determines which sheep is closest to it in terms of the Euclidean distance, and subsequently checks whether this sheep is within the range of its attack, that is whether the Euclidean distance to the sheep is not greater than the distance that the wolf moves when chasing a sheep; if this is the case, the wolf eats the sheep, which means that the sheep disappears and the wolf takes its position, whereas if this is not the case, the wolf starts chasing the sheep, moving a predefined distance towards it (if there are more than one sheep within the same closest distance, the wolf takes its actions with respect only to the first one). The simulation ends either when all sheep have been eaten or when a predefined maximum number of rounds has been reached.

## Requirements

- Implement a simulation as described above in an object-oriented manner, comprising at least two classes: one for a single sheep and the other for the wolf.
- The following values should be adopted:
  - Maximum number of rounds: 50
  - Number of sheep: 15
  - Absolute value of the limit imposed on each coordinate of the initial positions of sheep: 10.0
  - Distance of sheep movement: 0.5
  - Distance of wolf movement: 1.0
- Use the `random` module for generating random numbers and the `math` module for more advanced mathematical calculations.
- Display basic information about the status of the simulation at the end of each round:
  - Round number
  - Position of the wolf (to the third decimal place of each coordinate)
  - Number of alive sheep
  - If the wolf is chasing a sheep, indicate this fact along with the sequence number of the sheep
  - If a sheep was eaten, indicate this fact along with the sequence number of the sheep
- Use the `json` package to save the position of every animal at the end of each round to a `pos.json` file.
- Use the `csv` module to save the number of alive sheep at the end of each round to an `alive.csv` file.

# TASK 3 - Web Application for Storing Data and Machine Learning Predictions

## Overview

The task in this assignment is to develop a web application storing data that can be used for a machine learning model.

Data stored by the web application are a collection of data points that involve two or more continuous features and a single categorical feature. The exact names and the nature of these features do not matter and can be chosen arbitrarily. The data are supposed to be used for a classification task performed by a machine learning model that uses the continuous features to predict the corresponding category. The web application stores the data in a relational database consisting of a single table that holds individual data points as records.

In the basic version of the web application, data points can be retrieved from, added to, and deleted from the database. In the extended version of the web application, it is also possible to make predictions of the most likely category based on submitted values of the continuous features using a machine learning model.

### Requirements

- Implement the website part of the basic version of the web application.
- The web application should employ a database management system for managing a relational database with a single table.
- The website part should involve the following paths:
  - `/`: Displays all data points in the database.
  - `/add`: Adds a new data point to the database.
  - `/delete/<record_id>`: Deletes a data point from the database.
- Utilize object-relational mapping for mapping records in the database to objects in the code.
- Implement both the website and API parts of the extended version of the web application.
- The website part should involve a path: /predict: Predicts a category based on continuous features.
- The machine learning model predicting the category should be a k-nearest neighbors classifier.
- The API part should involve an endpoint: GET /api/predictions: Predicts a category based on continuous features.
- Utilize object-relational mapping for both website and API parts.


