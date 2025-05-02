returns the result of the ping operation.
    """
    url = request.args.get('url')
    if not url:
        return "Error: No URL provided. Please provide a URL as a query parameter.", 400

    # Sanitize the input to prevent command injection
    if any(c in url for c in [';', '&', '|', '`', '$', '>', '<']):
        return "Error: Invalid characters in URL.", 400

    try:
        # Perform the ping operation
        result = subprocess.run(
            ['ping', '-c', '4', url],  # '-c 4' sends 4 packets
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            return f"Ping successful:\n{result.stdout}", 200
        else:
            return f"Ping failed:\n{result.stderr}", 400
    except Exception as e:
        return f"Error occurred while trying to ping: {str(e)}", 500


# Initialize the Flask app
app = Flask(__name__)

if __name__ == "__main__":
    # Run the Flask app
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
```