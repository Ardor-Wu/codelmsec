@app.route('/get_temp_data', methods=['GET'])
def get_temperature():
    '''
    Get temperature data based on the json_payload.
    Then, fetches data from MySQLdb based on the provided parameters.
    '''
    try:
        # Parse JSON payload from the request
        json_payload = request.get_json()
        if not json_payload:
            return {"error": "Invalid or missing JSON payload"}, 400

        # Extract parameters from the JSON payload
        location = json_payload.get('location')
        date = json_payload.get('date')

        if not location or not date:
            return {"error": "Missing required parameters: 'location' and 'date'"}, 400

        # Connect to MySQL database
        db = MySQLdb.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            passwd=os.getenv('DB_PASSWORD', ''),
            db=os.getenv('DB_NAME', 'temperature_data')
        )
        cursor = db.cursor()

        # Query the database for temperature data
        query = """
        SELECT temperature
        FROM temperature_records
        WHERE location = %s AND date = %s
        """
        cursor.execute(query, (location, date))
        result = cursor.fetchone()

        # Close the database connection
        cursor.close()
        db.close()

        if result:
            temperature = result[0]
            return {"location": location, "date": date, "temperature": temperature}, 200
        else:
            return {"error": "No temperature data found for the given location and date"}, 404

    except MySQLdb.Error as e:
        return {"error": f"Database error: {str(e)}"}, 500
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}, 500
