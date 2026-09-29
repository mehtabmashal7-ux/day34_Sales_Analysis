Day 34 — Sales Analysis with Pandas
Project Overview
Day 34 Sales Analysis is a beginner-friendly data analysis project built using Python and Pandas.
The project reads sales data from a CSV file and analyzes revenue, products, quantities, cities, average sales, and individual sales records.
Objectives
Read and analyze CSV data
Calculate total sales and revenue
Analyze sales by product
Analyze sales by city
Analyze quantity sold
Find the highest-selling product
Find the city with the highest sales
Calculate average sales
Find the highest single sale
Sort sales results
Technologies Used
Python
Pandas
CSV
Project Structure
day34-sales-analysis/
│
├── sales.csv
├── Day34_Sales_Analysis.py
└── README.md
Dataset
The sales.csv file contains:
Column
Description
Date
Date of the sale
Product
Name of the product
Category
Product category
Quantity
Number of units sold
Price
Price per unit
City
City where the sale occurred
Sales Calculation
The project calculates total sales using:
Total Sales = Quantity × Price
Analysis Performed
Total Revenue
Calculates the total revenue generated from all sales.
Product Analysis
Groups sales by product and finds the product with the highest total sales.
City Analysis
Groups sales by city and finds the city with the highest total sales.
Quantity Analysis
Calculates the total quantity sold for each product and finds the most-sold product.
Average Sale
Calculates the average value of a sales transaction.
Highest Single Sale
Finds the highest individual sales transaction.
Sorting
Sorts products and cities by total sales from highest to lowest.
Pandas Concepts Used
pd.read_csv()
DataFrames
Creating new columns
groupby()
sum()
mean()
max()
idxmax()
sort_values()
Sample Results
Total Revenue: 511500

Highest Selling Product: Laptop
Highest Product Sales: 400000

Highest Sales City: Buner
Highest City Sales: 205000

Most Sold Product: Mouse
Units Sold: 13

Average Sale: 51150.0
Highest Single Sale: 160000
Products by Total Sales
Laptop      400000
Chair        49000
Table        24000
Keyboard     21000
Mouse        19500
Cities by Total Sales
Buner        205000
Peshawar     200000
Mansehra     108500
Installation
Install Pandas using:
python -m pip install pandas
How to Run
Open the project folder in VS Code and make sure these files are present:
sales.csv
Day34_Sales_Analysis.py
README.md
Run the program using:
python Day34_Sales_Analysis.py
Learning Outcomes
Through this project, I practiced:
Working with CSV files
Working with Pandas DataFrames
Creating calculated columns
Grouping data
Aggregating data
Finding maximum and average values
Sorting data
Performing basic real-world data analysis
Future Improvements
Add data visualization
Add monthly sales analysis
Add profit analysis
Analyze sales by category
Create an interactive dashboard
Project Status
Completed
Author
Mehtab Ahmad
License
This project is created for educational and learning purposes.