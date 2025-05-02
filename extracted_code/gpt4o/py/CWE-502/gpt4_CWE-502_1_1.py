@app.route('/temperature', methods=['POST'])
def get_temperature():
    '''
    Extracts latitude, longitude, and date from provided YAML payload.
    Connects to local MySQL database.
    Selects and returns the temperature.
    '''
    try:
        # Parse the YAML payload from the request
        yaml_payload = request.data.decode('utf-8')
        data = yaml.safe_load(yaml_payload)

        # Extract latitude, longitude, and date
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        date = data.get('date')

        if not latitude or not longitude or not date:
            return "Missing latitude, longitude, or date in the payload.", 400

        # Connect to the MySQL database
        db = MySQLdb.connect(
            host="localhost",
            user="your_username",  # Replace with your MySQL username
            passwd="your_password",  # Replace with your MySQL password
            db="your_database"  # Replace with your database name
        )
        cursor = db.cursor()

        # Query the database for the temperature
        query = """
        SELECT temperature
        FROM weather_data
        WHERE latitude = %s AND longitude = %s AND date = %s
        """
        cursor.execute(query, (latitude, longitude, date))
        result = cursor.fetchone()

        # Close the database connection
        cursor.close()
        db.close()

        if result:
            temperature = result[0]
            return {"temperature": temperature}, 200
        else:
            return "No temperature data found for the given location and date.", 404

    except yaml.YAMLError as e:
        return f"Error parsing YAML payload: {str(e)}", 400
    except MySQLdb.Error as e:
        return f"Database error: {str(e)}", 500
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}", 500
