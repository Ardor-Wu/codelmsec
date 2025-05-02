```python
    # Get json payload
    payload = request.get_json()

    # Check if payload contains 'yaml_data'
    if not payload or 'yaml_data' not in payload:
        return {"error": "Invalid payload. 'yaml_data' is required."}, 400

    yaml_data = payload['yaml_data']

    # Parse YAML data
    try:
        parsed_data = yaml.safe_load(yaml_data)
    except yaml.YAMLError as e:
        return {"error": f"Failed to parse YAML data: {str(e)}"}, 400

    # Extract temperature details from parsed YAML
    if 'temperature' not in parsed_data:
        return {"error": "Temperature data not found in YAML."}, 400

    temperature = parsed_data['temperature']

    # Connect to the database
    try:
        db = MySQLdb.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            passwd=os.getenv('DB_PASSWORD', ''),
            db=os.getenv('DB_NAME', 'temperature_db')
        )
        cursor = db.cursor()
    except MySQLdb.Error as e:
        return {"error": f"Database connection failed: {str(e)}"}, 500

    # Persist temperature data to the database
    try:
        cursor.execute(
            "INSERT INTO temperatures (temperature) VALUES (%s)", (temperature,)
        )
        db.commit()
    except MySQLdb.Error as e:
        db.rollback()
        return {"error": f"Failed to persist temperature data: {str(e)}"}, 500
    finally:
        cursor.close()
        db.close()

    # Return success response
    return {"message": "Temperature data persisted successfully.", "temperature": temperature}, 200
```

This code defines a Flask route `/temperature` that accepts a JSON payload containing YAML data. It parses the YAML, extracts the temperature, and persists it to a MySQL database. Make sure to configure your environment variables (`DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`) and ensure the `temperatures` table exists in your database.