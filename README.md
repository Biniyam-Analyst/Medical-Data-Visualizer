# Medical-Data-Visualizer
In this project, I analyzed a medical examination dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

📊 Project Overview
The goal was to visualize and examine medical data using Pandas, Matplotlib, and Seaborn. I performed data cleaning and created two main visualizations:

Categorical Plot: Shows the counts of good and bad health outcomes (cholesterol, glucose, smoking, alcohol use, physical activity, and overweight) split by whether the patients have cardiovascular disease or not.

Heat Map: A correlation matrix that shows how strongly different variables (like weight, height, and blood pressure) are related to each other.

🛠️ Technologies Used
Python

Pandas (Data manipulation)

Seaborn & Matplotlib (Data visualization)

NumPy (Mathematical operations)

🧼 Key Tasks Performed
Feature Engineering: Added an overweight column by calculating BMI.

Data Normalization: Standardized cholesterol and glucose data (0 for normal, 1 for high).

Data Cleaning: Filtered out incorrect blood pressure readings and extreme outliers in height and weight (outside the 2.5th and 97.5th percentiles).

Statistical Plotting: Created a long-format dataframe using pd.melt for categorical visualization.
