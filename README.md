# Website Traffic Sources Analysis and Visualization
A professional intermediate-level Python project for analyzing and visualizing website traffic data using real-world web analytics techniques. This project focuses on data cleaning, exploratory data analysis (EDA), business intelligence, and insightful visualizations to understand website performance and user engagement.

##  Project Overview

The **Website Traffic Sources Analysis and Visualization** project helps businesses and analysts understand:

* How website traffic changes over time
* Which traffic sources bring the most visitors
* Organic vs Paid traffic performance
* Conversion rates across different channels
* User engagement metrics such as bounce rate and session duration
* Device-wise and region-wise traffic distribution

The project reads traffic data from CSV files, performs preprocessing and EDA, generates professional visualizations, and exports analytical reports.

---
##  Features

### Data Cleaning and Preprocessing

* Handle missing values
* Remove duplicate records
* Validate and standardize date formats
* Normalize traffic source names
* Detect and handle inconsistent data

### Website Traffic Analysis

* Total Website Visits
* Monthly Traffic Trends
* Quarterly Traffic Analysis
* Yearly Traffic Growth
* Traffic Growth Rate (%)
* Average Daily Visitors

### Traffic Source Analysis

* Top Traffic Sources
* Organic vs Paid Traffic Comparison
* Conversion Rate by Source
* Bounce Rate Analysis
* Session Duration Analysis

### Device and Regional Analysis

* Device-wise Traffic:

  * Desktop
  * Mobile
  * Tablet

* Country-wise Traffic Distribution

* Region-wise Traffic Analysis

### Visualizations

Generate professional charts using Matplotlib:

* Line Charts for traffic trends
* Bar Charts for top traffic sources
* Pie Charts for traffic distribution
* Stacked Bar Charts for device-wise traffic
* Monthly and yearly comparison charts
* Correlation Heatmaps for engagement metrics

### Report Generation

* Export analysis reports to CSV files
* Save aggregated results in the `reports/` directory

##  Project Structure

```text
website-traffic-analysis/
│
├── traffic_analyzer.py
├── website_traffic.csv
├── requirements.txt
├── README.md
└── reports/
```

---

##  Technologies Used

* Python 3
* Pandas
* NumPy
* Matplotlib
* CSV
* Object-Oriented Programming (OOP)

---

##  Dataset Structure

The project uses a CSV dataset named:

```text
website_traffic.csv
```

### Sample Dataset

| Date       | Traffic_Source | Visits | Conversions | Bounce_Rate | Session_Duration | Device  | Country | Region      |
| ---------- | -------------- | -----: | ----------: | ----------: | ---------------: | ------- | ------- | ----------- |
| 2025-01-01 | Organic Search |   1200 |          85 |        42.5 |              4.8 | Desktop | India   | Maharashtra |
| 2025-01-01 | Social Media   |    800 |          35 |        55.2 |              3.2 | Mobile  | India   | Delhi       |
| 2025-01-02 | Paid Ads       |    950 |          60 |        47.1 |              3.9 | Desktop | USA     | California  |
| 2025-01-03 | Referral       |    500 |          25 |        58.0 |              2.8 | Tablet  | UK      | London      |

---

##  Visualizations

The project generates:

### 1. Traffic Trend Analysis

* Daily traffic trends
* Monthly traffic trends
* Quarterly traffic analysis
* Yearly traffic growth

### 2. Traffic Source Performance

* Top traffic sources
* Organic vs Paid traffic
* Conversion rate by source

### 3. User Engagement Analysis

* Bounce rate comparison
* Session duration analysis

### 4. Device and Region Analysis

* Device-wise traffic distribution
* Country-wise traffic analysis
* Region-wise traffic comparison

---

##  Terminal Dashboard

The application provides an interactive terminal menu:

```text
=========================================
 WEBSITE TRAFFIC ANALYSIS DASHBOARD
=========================================

1. View Dataset Summary
2. Analyze Traffic Trends
3. View Traffic Source Performance
4. Analyze Device-wise Traffic
5. Region-wise Traffic Analysis
6. Conversion and Bounce Rate Analysis
7. Generate Visualizations
8. Export Reports
9. Exit

Enter your choice:
```

---

## Reports

Generated reports are stored inside:

```text
reports/
```

Example reports:

* monthly_traffic_report.csv
* yearly_traffic_report.csv
* traffic_source_report.csv
* conversion_report.csv
* region_wise_report.csv

---

##  Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/website-traffic-analysis.git

cd website-traffic-analysis
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python traffic_analyzer.py
```

---

##  Key Business Insights

This project helps answer important business questions such as:

* Which traffic source generates the highest number of visitors?
* Is Organic traffic performing better than Paid traffic?
* Which regions contribute the most website visits?
* How does bounce rate vary across traffic sources?
* Which devices are most commonly used by visitors?
* What are the monthly and yearly growth trends?

---

##  Software Design

The project follows:

* Object-Oriented Programming (OOP)
* PEP 8 Coding Standards
* Modular Code Structure
* Exception Handling
* Input Validation
* Reusable Functions and Classes
* Comprehensive Comments and Docstrings

---

##  Future Enhancements

Potential improvements:

* Interactive Dashboard using Streamlit
* Real-time traffic monitoring
* Predictive traffic forecasting using Machine Learning
* Integration with Google Analytics API
* Interactive visualizations using Plotly
* Automated PDF report generation

AUTHOR : RUNZUN M. BHUTADA
INTERN-ID : CITS2504

