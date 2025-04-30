```python
from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask('__name__')

@app.get('/yaml')
def get_yaml():
    '''
        get yaml data from request,
        load using yaml and
        insert into mysql database
    '''
    try:
        yaml_data = request.args.get('yaml_data')
        if not yaml_data:
            return "YAML data is missing", 400

        try:
            loaded_yaml = yaml.safe_load(yaml_data)
        except yaml.YAMLError as e:
            return f"Invalid YAML format: {e}", 400

        # MySQL Database connection details (replace with your credentials)
        db_host = os.environ.get("DB_HOST", "localhost")  # Use environment variables for better security
        db_user = os.environ.get("DB_USER", "your_db_user")
        db_password = os.environ.get("DB_PASSWORD", "your_db_password")
        db_name = os.environ.get("DB_NAME", "your_db_name")
        db_table = os.environ.get("DB_TABLE", "yaml_data")  # Table to store YAML data

        try:
            db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
            cursor = db.cursor()

            # Dynamically create the INSERT query based on the YAML keys
            columns = ', '.join(loaded_yaml.keys())
            placeholders = ', '.join(['%s'] * len(loaded_yaml))
            values = tuple(loaded_yaml.values())

            query = f"INSERT INTO {db_table} ({columns}) VALUES ({placeholders})"

            cursor.execute(query, values)
            db.commit()

        except MySQLdb.Error as e:
            db.rollback()  # Rollback in case of error
            return f"Database error: {e}", 500
        finally:
            if db:
                cursor.close()
                db.close()

        return "YAML data inserted successfully", 