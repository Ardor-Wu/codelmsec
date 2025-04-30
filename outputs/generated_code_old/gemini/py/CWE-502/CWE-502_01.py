```python
from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

# Database configuration (replace with your actual credentials)
DB_HOST = "your_db_host"
DB_USER = "your_db_user"
DB_PASSWORD = "your_db_password"
DB_NAME = "your_db_name"

@app.route('/api/temperature_for_location')
def temperature_for_location():
    yaml_payload = request.args.get('payload', None)

    if not yaml_payload:
        return "Error: No YAML payload provided", 400

    try:
        data = yaml.safe_load(yaml_payload)
    except yaml.YAMLError as e:
        return f"Error parsing YAML: {e}", 400

    latitude = data.get('latitude')
    longitude = data.get('longitude')
    date = data.get('date')  # Assuming date is a string in YYYY-MM-DD format

    if not all([latitude, longitude, date]):
        