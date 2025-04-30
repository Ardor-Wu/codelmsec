```python
from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb


app = Flask(__name__)
app.config['DEBUG'] = True
@app.route("/yaml")
def yaml_return():
    """
    Get data from request, load YAML data from it, and insert into MySQL.
    """
    try:
        yaml_data = request.get_data().decode('utf-8')  # Decode from bytes to string
        data = yaml.safe_load(yaml_data)

        # Database credentials (replace with your actual credentials)
        db_host = os.environ.get("DB_HOST", "localhost")  # Get from environment variables or default
        db_user = os.environ.get("DB_USER", "your_db_user")
        db_password = os.environ.get("DB_PASSWORD", "your_db_password")
        db_name = os.environ.get("DB_NAME", "your_db_name")
        db_table = os.environ.get("DB_TABLE", "your_db_table") # Get table name


        db = MySQLdb.connect(host=db_host, user=db_user, password=db_password, database=db_name)
        cursor = db.cursor()

        # Dynamically build the insert query based on the YAML data
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        values = tuple(data.values())

        sql = f"INSERT INTO {db_table} ({columns}) VALUES ({placeholders})"

        cursor.execute(sql, values)
        db.commit()
        cursor.close()
        db.close()

        return "YAML data inserted successfully!", 200

    except yaml.YAMLError as e:
        return f"Error parsing YAML: {e}", 400
    except MySQLdb.Error as e:
        return f"MySQL error: {e}", 500 # 500 for server error
    except Exception as e: # Catch other potential errors
        return f"An unexpected error occurred: {e}", 500




if __name__ == "__main