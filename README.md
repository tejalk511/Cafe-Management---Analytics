# Coffee Shop Management System

## Description

This project is a Streamlit-based web application designed to manage coffee shop sales records. It provides an interactive interface for users to view, add, delete, and modify coffee orders. The application uses a SQL database to store and retrieve sales data, making it easy to keep track of all transactions.

## Setup Instructions

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/coffee-shop-management.git
   cd coffee-shop-management
   ```

2. **Install the Required Dependencies**:
   Make sure you have Python installed. Then, install the dependencies using pip:
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Streamlit Application**:
   Start the Streamlit server to run the application:
   ```sh
   streamlit run test_streamlit_sql.py
   ```

## Usage

1. **Open the Application**:
   Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

![home](https://github.com/user-attachments/assets/d1fb311e-48c6-4c55-82d9-cb8cfd0d3f5c)

2. **Navigate Using the Sidebar**:
   Use the sidebar to navigate between different options:
   - **Home**: View the welcome page.
   - **Show All Sales**: View all sales records.
   - **Add Coffee Order**: Add a new coffee order.
   - **Delete Record**: Delete an existing coffee order.
   - **Modify Order Records**: Update existing sales records.

3. **Add a Coffee Order**:
   - Select "Add Coffee order" from the sidebar.
   - Enter the order details such as date, time, payment method, card details, bill amount, and coffee type.
   - Click the "Add Order Entry" button to save the order.
   
![Add_sales_order](https://github.com/user-attachments/assets/497a9d75-9af7-4fca-8a47-184205d67887)

4. **Delete a Coffee Order**:
   - Select "Delete Record" from the sidebar.
   - Enter the details of the order to be deleted.
   - Click the "Delete" button to remove the order from the database.

5. **Modify Order Records**:
   - Select "Modify Order Records" from the sidebar.
   - Follow the prompts to update existing sales records.

![Modify_sales_record2](https://github.com/user-attachments/assets/5c664e49-eefc-4cac-add0-c7791c80f5b4)

6. **Sales DashBoard**:
- Swipe left or right to view different sales dashboard results.
- You can zoom in and out to explore the details more clearly and open specific sections for further insights.
![Sales_analyer](https://github.com/user-attachments/assets/ddfc44a0-aef4-4810-864b-3f46d44949ef)

## Contributor Guidelines

We welcome contributions to improve this project. To contribute, please follow these steps:

1. **Fork the Repository**:
   Click the "Fork" button at the top right of the repository page to create a copy of the repository in your GitHub account.

2. **Clone Your Fork**:
   Clone your forked repository to your local machine:
   ```sh
   git clone https://github.com/yourusername/coffee-shop-management.git
   cd coffee-shop-management
   ```

3. **Create a Branch**:
   Create a new branch for your feature or bug fix:
   ```sh
   git checkout -b feature-or-bugfix-name
   ```

4. **Make Your Changes**:
   Make your changes to the codebase.

5. **Commit Your Changes**:
   Commit your changes with a descriptive commit message:
   ```sh
   git commit -m "Description of the changes"
   ```

6. **Push to Your Fork**:
   Push your changes to your forked repository:
   ```sh
   git push origin feature-or-bugfix-name
   ```

7. **Create a Pull Request**:
   Open a pull request from your forked repository to the main repository. Provide a clear description of your changes and any relevant information.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
