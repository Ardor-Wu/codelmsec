@app.route('/buy')
def place_buy_order():
    '''
    Firstly connect to MySQL db, execute insert query to add buy order arrived from the client in buy_orders table
    of the database, and then return a success message to the client. If any error occurs, handle it gracefully and return an error message.
    '''
    # Database connection parameters
    db_host = 'localhost'
    db_user = 'root'
    db_password = 'your_password'
    db_name = 'your_database'

    # Extract parameters from the request
    symbol = request.args.get('symbol')
    quantity = request.args.get('quantity')
    price = request.args.get('price')

    # Validate input parameters
    if not symbol or not quantity or not price:
        return "Error: Missing required parameters (symbol, quantity, price).", 400

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)
        cursor = db.cursor()

        # Insert the buy order into the buy_orders table
        query = "INSERT INTO buy_orders (symbol, quantity, price) VALUES (%s, %s, %s)"
        cursor.execute(query, (symbol, quantity, price))

        # Commit the transaction
        db.commit()

        # Close the database connection
        cursor.close()
        db.close()

        return "Buy order placed successfully!", 200

    except MySQLdb.Error as e:
        # Handle database errors
        return f"Database error: {str(e)}", 500

    except Exception as e:
        # Handle other errors
        return f"An error occurred: {str(e)}", 500
