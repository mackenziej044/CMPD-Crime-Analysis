# Import Flask and other necessary libraries
from flask import Flask, jsonify
import pandas as pd 
import sqlite3

app = Flask(__name__)

# Create connection and cursor function
def get_db_connection():
    conn = sqlite3.connect('cmpd_data.db')
    conn.row_factory = sqlite3.Row  # This allows us to return rows as dictionaries
    return conn

# Create table if it doesn't exist
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS cmpd_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        incident_type TEXT NOT NULL,
        date TEXT NOT NULL,
        location TEXT NOT NULL,
        description TEXT
    );
    '''
    
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()

# Call the function to create the table
create_table()

# file path
file_path = '/Users/mackenzie/Documents/GitHub/CMPD-Crime-Analysis/Crime Data/cmpd.csv'

# Function to import data from a CSV file into the table
def import_data_from_csv(file_path):
    try:
        conn = get_db_connection()
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Insert data into the cmpd_data table
        df.to_sql('cmpd_data', conn, if_exists='append', index=False)
        print(f"Successfully imported {len(df)} records from {file_path}.")
        
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        print("Error: There was a problem parsing the file.")
    except Exception as e:
        print(f"An error occurred while importing data: {e}")
    finally:
        conn.close()

# Call this function to import data from your CSV file
import_data_from_csv('cmpd.csv')

# Define a function to fetch data from the database
def fetch_data(print_function):
    conn = get_db_connection()
    crime_df = pd.read_sql_query('SELECT * FROM cmpd_data', conn)
    conn.close()
    return crime_df

# Define endpoints
@app.route('/data', methods=['GET'])
def get_data():
    crime_df = fetch_data()
    data = crime_df.to_dict(orient='records')
    # return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
