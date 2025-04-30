```python
from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb
app = Flask(__name__)

@app.route('/temperature')
def getYamlTemperature():
    '''
    Parse temperature details from the given YAML load and return
    the persisted temperature from the database.
    '''

    # Get json payload
    try:
        yaml_data = request.get_json()
    except Exception as e:
        return f"Invalid YAML input: {e}", 400

    try:
        # Parse YAML data
        loaded_yaml = yaml.safe_load(yaml_data)
    except yaml.YAMLError as e:
        return f"Error parsing YAML: {e}", 400

    try:
        temperature = loaded_yaml['temperature']
    except KeyError:
        return "Temperature key not found in YAML", 400


    # Database connection details (replace with your actual credentials)
    db_config = {
        'host': 'your_db_host',  # Replace with your DB host
        'user': 'your_db_user',  # Replace with your DB user
        'password': 'your_db_password', # Replace with your DB password
        'database': 'your_db_name' # Replace with your DB name
    }

    try:
        # Establish database connection
        db = MySQLdb.connect(**db_config)
        cursor = db.cursor()

        # Insert temperature into the database (assuming a table named 'temperatures' exists)
        cursor.execute("INSERT INTO temperatures (temperature) VALUES (%s)", (temperature,))
        db.commit()

        # Retrieve the last inserted temperature (you might need to adapt this based on your DB structure)
        cursor.execute("SELECT temperature FROM temperatures ORDER BY id DESC LIMIT 1")
        persisted_temperature = cursor.fetchone()[0]


    except MySQLdb.Error as e:
        return f"Database error: {e}", 500
    finally:
        if db:
            cursor.close()
            db.close()



    return str(persisted_temperature), 200



if __name__ == '__main__':
    app.run(debug=True)

```

