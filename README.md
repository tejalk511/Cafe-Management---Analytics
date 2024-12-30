# Cafe-Management-Analytics

# Coffee Shop Management System
This project is a Streamlit-based web application for managing coffee shop sales records. It allows users to view, add, delete, and modify coffee orders. The application uses a SQL database to store and retrieve sales data.

## Features
- Home: Welcome page with a brief introduction and navigation instructions.
- Show All Sales: Displays all sales records from the database.
- Add Coffee Order: Allows users to add a new coffee order with details such as date, time, payment method, card details, bill amount, and coffee type.
- Delete Record: Enables users to delete a specific coffee order based on date, coffee type, payment method, and card details.
- Modify Order Records: Provides functionality to update existing sales records.

## Dependencies
The project relies on the following dependencies:
Streamlit: For creating the web application interface.
Pandas: For data manipulation and analysis.
SQLite: For database operations.
Datetime: For handling date and time operations.
UUID: For generating unique keys.
Typing: For type hinting.


## Installation
Clone the repository:
git clone https://github.com/yourusername/coffee-shop-management.git
cd coffee-shop-management

## Install the required dependencies:
pip install -r requirements.txt

## Run the Streamlit application:
streamlit run test_streamlit_sql.py

## Usage
Open the application in your web browser.
Use the sidebar to navigate between different options:
Home: View the welcome page.
Show All Sales: View all sales records.
Add Coffee Order: Add a new coffee order.
Delete Record: Delete an existing coffee order.
Modify Order Records: Update existing sales records.
