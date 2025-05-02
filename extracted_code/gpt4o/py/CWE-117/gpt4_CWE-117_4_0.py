name)
    return f"Username {name} logged successfully."
    
# Initialize the Flask application
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    app.run(debug=True)
