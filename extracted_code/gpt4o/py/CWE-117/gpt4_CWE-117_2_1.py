current_app.logger.error(f"User input received: {user_input}")
    return "Input logged successfully.", 200

if __name__ == '__main__':
    app.run(debug=True)
