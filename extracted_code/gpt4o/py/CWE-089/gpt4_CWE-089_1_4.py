def submit_order():
    """
    Establishes a connection with MySQL database and submits a buy order.
    """
    # Extract order details from the request
    try:
        order_data = request.json
        if not order_data:
            return {"error": "Invalid input. Expected JSON data."}, 400

        user_id = order_data.get("user_id")
        stock_symbol = order_data.get("stock_symbol")
        quantity = order_data.get("quantity")
        price = order_data.get("price")

        if not all([user_id, stock_symbol, quantity, price]):
            return {"error": "Missing required fields: user_id, stock_symbol, quantity, price."}, 400

        # Connect to the MySQL database
        db = MySQLdb.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            passwd=os.getenv("DB_PASSWORD", ""),
            db=os.getenv("DB_NAME", "trading_db")
        )
        cursor = db.cursor()

        # Insert the buy order into the database
        query = """
        INSERT INTO buy_orders (user_id, stock_symbol, quantity, price, status)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (user_id, stock_symbol, quantity, price, "PENDING"))
        db.commit()

        # Get the ID of the newly inserted order
        order_id = cursor.lastrowid

        # Close the database connection
        cursor.close()
        db.close()

        # Call the order_filled script asynchronously
        script_path = os.path.join(os.path.dirname(__file__), "order_filled.py")
        subprocess.Popen([sys.executable, script_path, str(order_id)])

        return {"message": "Buy order submitted successfully.", "order_id": order_id}, 200

    except MySQLdb.Error as e:
        return {"error": f"Database error: {str(e)}"}, 500
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}, 500
