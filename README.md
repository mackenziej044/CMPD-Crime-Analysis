# CMPD-Crime-Analysis
# Analyzing and Predicting Crime Trends in Charlotte, NC Using Machine Learning

## Objective
This project leverages machine learning and data analysis to uncover crime trends within Charlotte, NC. By analyzing historical data from the Charlotte-Mecklenburg Police Department (CMPD), we aim to:

1. Identify patterns in crime occurrences based on time, location, and type.
2. Develop predictive models to forecast violent crime trends.
3. Present insights through an interactive dashboard or web application for law enforcement, community leaders, and policymakers.

---
## Tableau Public
Tableau Vizualizations uploaded to Tableau Public: https://public.tableau.com/shared/XTSJT9M73?:display_count=n&:origin=viz_share_link

## Dataset
We are utilizing publicly available CMPD Crime Incident Data from the [Charlotte Open Data Portal](https://data.charlottenc.gov/datasets/charlotte%3A%3Acmpd-incidents-1/about?utm_source=chatgpt.com).

**Key Features:**
- Crime Type
- Incident Date and Time
- Location (latitude and longitude)
- Arrest Status
- Neighborhood
- Weapon Involved

**Secondary Data Source:**
Police Division boundary coordinates from [Koordinates](https://koordinates.com/layer/96916-charlotte-nc-police-divisions/).

---

## Research Questions
1. What are the most frequent types of crimes in Charlotte, and how do they vary over time and across neighborhoods?
2. Which neighborhoods have the highest concentration of specific crime types?
3. How do factors like time of day, day of the week, or seasonality influence crime trends?
4. Can a machine learning model predict the type of crime likely to occur based on time and location?

---

## Tools and Technologies
1. **Data Analysis**: Python (Pandas)
2. **Machine Learning**: Scikit-learn
3. **Database**: SQLite
4. **Visualization**: Tableau Public or Flask with JavaScript (Leaflet.js or Plotly)

---

## Methodology

### 1. Data Cleaning and Preprocessing
- Handle missing or inconsistent data.
- Parse timestamps to extract useful features like hour, day of the week, and season.
- Group and simplify crime categories (e.g., violent, property, other).

### 2. Exploratory Data Analysis (EDA)
- Visualize crime frequency by type, time, and location.
- Identify crime hotspots using spatial mapping techniques.

### 3. Machine Learning Model Development
- Train a classification model (e.g., Random Forest or Decision Tree) to predict crime types based on location and time.
- Evaluate model performance using metrics such as accuracy, precision, and recall.

### 4. Visualization and Insights
- Create interactive visualizations of crime trends and predictions.
- Develop a user-friendly dashboard or web app for exploring data and predictions.

---

## Deliverables
1. **Predictive Model**: A trained machine learning model capable of forecasting crime violent trends.
2. **Interactive Dashboard/Web App**: A tool for exploring data trends and predictions.
3. **Final Presentation**: Summary of findings, methodologies, and recommendations for community and policy improvement.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd crime-trends-project
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database by importing the cleaned dataset into SQLite:
   ```bash
   sqlite3 crime_data.db < crime_data.sql
   ```

4. Run the Flask application (if using Flask for visualization):
   ```bash
   python app.py
   ```

---

## Usage
1. Access the interactive dashboard via your local server (e.g., `http://127.0.0.1:5000`).
2. Explore crime trends using filters such as time, location, or crime type.
3. View predictive model results and insights for future trends.

---
## Machine Learning
### Overview of the Model
The SARIMA crime forecasting model was developed to predict monthly violent crime counts in Charlotte, NC, using historical data from 2017 to 2024. The primary goal of the model is to analyze crime trends and forecast crime counts for the next year (2024-2025) to aid decision-making by the Charlotte-Mecklenburg Police Department (CMPD) and other stakeholders.
The model utilizes seasonality, trend analysis, and historical patterns to provide actionable insights. It was optimized iteratively to improve accuracy and performance metrics, ensuring it meets the project's requirements.

Copy of full report with model analysis, optimization process, and result debrif are linked below:
https://github.com/mackenziej044/CMPD-Crime-Analysis/blob/4683b0ef84d58eae0d9bf8425f38040755955775/CMPD%20TIME%20SERIES%20DATA%20ANALYSIS/Crime%20Forecasting%20Model%20Report%20(1).pdf

---

## Team
- [Kelly Brookshire] - Tableau Specialist
- [Mackenzie Jarrett] - HTML and Backend
- [Leonardo Francisco] - Machine Learning Model

---

## License
This project is licensed under the MIT License. See `LICENSE` for details.
