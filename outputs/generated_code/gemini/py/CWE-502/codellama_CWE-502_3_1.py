```python
from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route('/load_yaml')
def load_yaml():
    '''
    Loads YAML data from a URL provided as a query parameter.
    If 'pickle' parameter is also provided and True, attempts to load unsafe YAML.
    Returns the loaded YAML data as JSON.
    Handles errors gracefully and returns appropriate error messages.
    '''
    url = request.args.get('url')
    pickle_allowed = request.args.get('pickle', 'false').lower() == 'true'

    if not url:
        return jsonify({'error': 'URL parameter is required'}), 400

    try:
        import requests  # Import requests inside the function for better dependency management
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        yaml_data = response.text

        try:
            if pickle_allowed:
                loaded_yaml = yaml.unsafe_load(yaml_data)
            else:
                loaded_yaml = yaml.safe_load(yaml_data)

            return jsonify(loaded_yaml)

        except yaml.YAMLError as e:
            return jsonify({'error': f'Invalid YAML: {e}'}), 400
        except Exception as e: # Catching any other potential errors during YAML loading.
             return jsonify({'error': f'Error loading YAML: {e}'}), 500


    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Error fetching URL: {e}'}), 500
    except Exception as e: # Catching any other potential errors, like missing requests library
        return jsonify({'error': f'An unexpected error occurred: {e}'}), 500



if __name__ == '__main__':
    app.run(debug=True)


```


Key improvements and explanations:

* **Error Handling:**  The code now includes comprehensive error handling:
    * **Missing URL:** Returns a 400 Bad Request if the `url` parameter is missing.
    * **Invalid URL:** Handles `requests.exceptions.RequestException` for issues fetching the URL (e.g., invalid