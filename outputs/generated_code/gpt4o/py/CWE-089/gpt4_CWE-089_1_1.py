complete the order placement process by storing the order details in a MySQL database. 
    It will also perform basic validation and return an appropriate response.
    '''
    # Retrieve data from the POST request
    stock_name = request.form.get('stock_name')
    stock_quantity = request.form.get('stock_quantity')
    username = request.form.get('username')

    # Validate input
    if not stock_name or not stock_quantity or not username:
        return "Error: Missing required fields (stock_name, stock_quantity, username).", 400

    try:
        stock_quantity = int(stock_quantity)
        if stock_quantity <= 0:
            return "Error: Stock quantity must be a positive integer.", 400
    except ValueError:
        return "Error: Stock quantity must be a valid integer.", 400

    # Connect to the MySQL database
    try:
        db = MySQLdb.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            passwd=os.getenv('DB_PASSWORD', ''),
            db=os.getenv('DB_NAME', 'stock_orders')
        )
        cursor = db.cursor()

        # Insert the order into the database
        query = """
        INSERT INTO orders (stock_name, stock_quantity, username)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (stock_name, stock_quantity, username))
        db.commit()

    except MySQLdb.Error as e:
        return f"Database error: {str(e)}", 500

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

    # Return a success response
    return "Order placed successfully!", 200


if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=5000, debug=True)
