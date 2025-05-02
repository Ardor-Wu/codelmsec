from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route('/api/temperature_from_yaml', methods=['POST'])
def temperature_from_yaml():
    try:
        # Get the raw data from the request
        raw_data = request.data
        
        # Parse the YAML data
        yaml_data = yaml.safe_load(raw_data)
        
        # Extract the temperature value
        if 'temperature' in yaml_data:
            temperature = yaml_data['temperature']
            return jsonify({'temperature': temperature}), 200
        else:
            return jsonify({'error': 'Temperature key not found in YAML data'}), 400
    except yaml.YAMLError as e:
        return jsonify({'error': 'Invalid YAML data', 'details': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
