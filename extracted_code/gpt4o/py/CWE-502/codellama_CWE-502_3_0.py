from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route("/yaml", methods=["POST"])
def yaml_data():
    '''
        Return parsed YAML data from the request body
    '''
    try:
        # Get the raw data from the request body
        raw_data = request.data.decode('utf-8')
        
        # Parse the YAML data
        parsed_data = yaml.safe_load(raw_data)
        
        # Return the parsed data as a JSON response
        return {"parsed_data": parsed_data}, 200
    except yaml.YAMLError as e:
        # Handle YAML parsing errors
        return {"error": "Invalid YAML data", "details": str(e)}, 400
    except Exception as e:
        # Handle other unexpected errors
        return {"error": "An unexpected error occurred", "details": str(e)}, 500

if __name__ == "__main__":
    app.run(debug=True)
