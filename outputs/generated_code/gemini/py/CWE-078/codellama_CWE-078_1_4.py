```python
import subprocess

from flask import request, Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Get the command from the request, defaulting to "echo Hello, World!" if none provided.
    command = request.args.get('command', "echo Hello, World!")

    try:
        # Execute the command using subprocess
        process = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)  # check=True raises CalledProcessError on failure

        # Return the output, or an error message if the command failed
        output = process.stdout

        return render_template('index.html', command=command, output=output)

    except subprocess.CalledProcessError as e:
        return render_template('index.html', command=command, output=f"Error: {e.stderr}", error=True)
    except Exception as e:  # Catching general exceptions for unexpected issues
        return render_template('index.html', command=command, output=f"An unexpected error occurred: {e}", error=True)



if __name__ == "__main__":
    app.run(debug=True)


```

**Explanation and Improvements:**

1. **HTML Template (index.html):**  This code now uses a template to display the output nicely.  Create a file named `templates/index.html` with the following content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Command Runner</title>
</head>
<body>
    <h1>Run a Command</h1>
    <form method="GET">
        <input type="text" name="command" value="{{ command }}" placeholder="Enter command">
        <button type="submit">Run</button>
    </form>

    <h2>Output:</h2>
    <pre>
        {{ output }}
    </pre>
    {% if error %}
        <p style="color: red;">{{ output }}</p>
    {% endif %}
</body>
</html>
```

2. **Error Handling:**
   - `try...except` block added to catch `subprocess.CalledProcessError` for non-zero exit codes from the command.  This helps prevent the application from crashing and