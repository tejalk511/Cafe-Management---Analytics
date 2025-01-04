import base64
import os
import pyodbc
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import requests
import datetime
from PIL import Image

SERVER = 'XXXXXXXX'
DATABASE = 'COFFEE_SALES'
USERNAME = 'xxxxxx'
PASSWORD = '******'

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

def loti(url):
    r = requests.get(url)
    if r.status_code != 200:
       return None
    else:
        return r.json()


#@st.cache_resource
def init_connection():
    return pyodbc.connect(connectionString)

conn = init_connection()


def show_all_sales(db):
    print("Checkpoint 1 \n")
    cur = db.cursor()
    print("Checkpoint 2 \n")
    # Select the database
    #cur.execute("USE coffee_db")
    select_query = """
    SELECT * from coffee_db
    """
    print("Checkpoint 3.1 \n")
    cur.execute(select_query)

    # Set display options to increase the number of rows and columns
    pd.set_option('display.max_rows', 100)  # Adjust as needed
    pd.set_option('display.max_columns', 20)  # Adjust as needed
    pd.set_option('display.width', 5000)  # Set the width of the display
    pd.set_option('display.max_colwidth', 200)  # Set maximum column width

    df = pd.read_sql_query(select_query, conn)
    st.write(df)
    # If no records found, show a message
    if df.empty:
        st.write("No sales records found.")
        return



    

def insert_order_record(date1, datetime1, cash_or_card, card_details, total_money, coffee):
    """Insert a new patient record into the 'patients' table."""
    cursor = db.cursor()

    insert_orders_query = """
    INSERT INTO coffee_db (date, datetime, cash_type, card, money, coffee_name)
    VALUES (?, ?, ?, ?, ?, ?)
    """

    sales_data = (date1, datetime1, cash_or_card, card_details, total_money, coffee)

    cursor.execute(insert_orders_query, sales_data)
    db.commit()
    st.write("Coffee order record inserted successfully.") 


def delete_order_record(db, del_date1, del_cash_or_card, del_card, del_coffee):
    """Delete a patient record from the 'patients' table based on ID, name, or contact number."""
    cursor = db.cursor()

    delete_patient_query = """
    DELETE FROM coffee_db WHERE date = ? AND cash_type = ? AND  card = ? AND coffee_name = ?
    """

    delete_value = del_date1, del_cash_or_card, del_card, del_coffee

    cursor.execute(delete_patient_query, delete_value)
    db.commit()
    st.write("Patient record deleted successfully.")


def update_sales_record(db):
    """Search for a single record and allow editing of only the selected tuple."""
    
    st.subheader("Search and Edit a Single Record")

    # Database cursor
    cur = db.cursor()

    # Input fields for filtering records
    st.write("Search for a specific record using any of the following keys:")
    date_filter = st.date_input("Enter Date (YYYY-MM-DD)", key="date_filter")
    payment_options = ['Cash', 'Card']
    cash_type_filter = st.selectbox("Enter Cash Type", key="cash_type_filter", options=payment_options)
    menu_options = ['Latte', 'Cappuccino', 'Cocoa', 'Americano with Milk', 'Cortado', 'Espresso', 'Americano', 'Hot Chocolate']
    coffee_name_filter = st.selectbox("Enter Coffee Name", key="coffee_name_filter", options=menu_options)

    # Add a Search button
    if st.button("Search Records"):
        # Build the WHERE clause for filtering
        where_clause = "WHERE 1=1"  # Default WHERE clause (always true)
        if date_filter:
            where_clause += f" AND date = '{date_filter}'"
        if cash_type_filter:
            where_clause += f" AND cash_type = '{cash_type_filter}'"
        if coffee_name_filter:
            where_clause += f" AND coffee_name = '{coffee_name_filter}'"

        # Execute query to fetch filtered records
        query = f"SELECT * FROM coffee_db {where_clause}"
        df = pd.read_sql_query(query, db)

        # If no records found, display a message
        if df.empty:
            st.write("No records found for the given filters.")
            return

        # Save the search results to session state
        st.session_state['search_results'] = df

    # Check if search results exist in session state
    if 'search_results' in st.session_state:
        df = st.session_state['search_results']

        # Display the DataFrame
        st.write("Search Results:")
        st.dataframe(df)

        # Select box to choose a specific row (persist selection using session state)
        if 'selected_row_index' not in st.session_state:
            st.session_state['selected_row_index'] = None

        row_selection = st.selectbox(
            "Select a record to edit:",
            options=df.index,
            format_func=lambda idx: f"Row {idx + 1}: {df.loc[idx, 'date']}, {df.loc[idx, 'cash_type']}, {df.loc[idx, 'coffee_name']}",
            key="row_selection",
        )

        # Update session state when a row is selected
        st.session_state['selected_row_index'] = row_selection

        # Ensure a record is selected before editing
        if st.session_state['selected_row_index'] is not None:
            selected_row = df.loc[st.session_state['selected_row_index']]

            # Editable fields for the selected record
            st.write("Edit Selected Record:")
            date = st.text_input("Date", selected_row['date'], key="edit_date")
            cash_type = st.text_input("Cash Type", selected_row['cash_type'], key="edit_cash_type")
            coffee_name = st.text_input("Coffee Name", selected_row['coffee_name'], key="edit_coffee_name")
            total_money = st.number_input("Total Money", selected_row['money'], key="edit_money")

            # Update button
            if st.button("Update Record"):
                update_query = """
                UPDATE coffee_db
                SET date = ?, cash_type = ?, coffee_name = ?, money = ?
                WHERE id = ?
                """
                cur.execute(update_query, (date, cash_type, coffee_name, total_money, selected_row['id']))
                db.commit()
                st.success("Record updated successfully!")

                # Clear session state to refresh data
                del st.session_state['search_results']
                del st.session_state['selected_row_index']
                st.write("Please search again to view the updated record.")

        # Add a Reset button to clear search results and selection
        if st.button("Reset Search Records"):
            if 'search_results' in st.session_state:
                del st.session_state['search_results']
            if 'selected_row_index' in st.session_state:
                del st.session_state['selected_row_index']
            st.write("Search reset successfully. You can perform a new search.")


# List of image paths
image_paths = ["ilovepdf_pages-to-jpg\power_bi_report2_page-0001.jpg", "ilovepdf_pages-to-jpg\power_bi_report2_page-0002.jpg"]  # Replace with your image file paths

def view_analysis_db(db):
    # Initialize session state to track the current image index
    if "current_index" not in st.session_state:
        st.session_state.current_index = 0

    # Display the current image
    image = Image.open(image_paths[st.session_state.current_index])
    st.image(image, caption=f"Image {st.session_state.current_index + 1} of {len(image_paths)}", use_column_width=True)

    # Navigation buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("⬅️ Previous", key="prev"):
            st.session_state.current_index = (st.session_state.current_index - 1) % len(image_paths)
    with col3:
        if st.button("Next ➡️", key="next"):
            st.session_state.current_index = (st.session_state.current_index + 1) % len(image_paths)



def main():
    # Title and sidebar
    st.title("BrewBiz: Coffee Sales Analyzer")
    lott1 = loti("https://lottie.host/2fab43a9-afe3-4e18-9b32-26ec11cb9541/ePl7AwSWZP.json")

    menu = ["Home","Show All Sales", "Add Coffee order", "Delete Record", "Modify Order Records","View Analysis"]
    
    options = st.sidebar.radio("Select an Option :dart:",menu)
    if options== "Home":
        st.subheader("Welcome to Coffee Shop management system")
        st.write("Navigate from sidebar to access database")
        st_lottie(lott1,height=500)
       

    elif options=="Show All Sales":
        show_all_sales(db)

    
    elif options == "Add Coffee order":
       st.subheader("Enter coffee order details - ")
       #st_lottie(lotipatient,height = 200)
       date1 = st.date_input("Enter date",key = "date1")
       time1 = st.time_input("Enter time",key = "time1")
       datetime1 = datetime.datetime.combine(date1, time1)
       payment_options = ['Cash', 'Card']
       cash_or_card = st.selectbox("Payment method",key = "cash_or_card", options=payment_options)
       card_details = st.text_input("card",key = "card_details")
       total_money = st.number_input("Enter Bill amount",key= "total_money", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
       menu_options = ['Latte', 'Cappuccino', 'Cocoa', 'Americano with Milk', 'Cortado', 'Espresso', 'Americano', 'Hot Chocolate']
       coffee = st.selectbox("Choose coffee to order ",key= "coffee", options=menu_options)
       if st.button("Add Order Entry"):
          cursor = db.cursor()
          insert_order_record(date1, datetime1, cash_or_card, card_details, total_money, coffee)

        
    elif options == "Delete Record":
        st.subheader("Search a record to delete: ")
        del_date1 = st.date_input("Enter date",key = "date1")
        menu_options = ['Latte', 'Cappuccino', 'Cocoa', 'Americano with Milk', 'Cortado', 'Espresso', 'Americano', 'Hot Chocolate']
        del_coffee = st.selectbox("Choose coffee to order ",key= "coffee", options=menu_options)
        payment_options = ['Cash', 'Card']
        del_cash_or_card = st.selectbox("Payment method",key = "cash_or_card", options=payment_options)
        del_card = st.text_input("card",key = "card_details")

        if st.button("Delete"):
            delete_order_record(db, del_date1, del_cash_or_card, del_card, del_coffee)
    
    elif options == "Modify Order Records":
        update_sales_record(db)
    
    elif options == "View Analysis":
        view_analysis_db(db)

    db.close()


if __name__ == "__main__":
    db = init_connection()
    main()
