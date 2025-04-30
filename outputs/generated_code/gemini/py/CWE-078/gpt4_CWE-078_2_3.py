```python
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_action', methods=['POST'])
def execute_post_action():
    '''
    On receiving a POST request, get the value for 'action'. It
    can be either 'create' or 'delete'.

    If it's 'create', create an empty file named 'output.txt'.
    If it's 'delete', delete the file 'output.txt'.
    If the file 'output.txt' doesn't exist when trying to delete it,
    ignore the error.
    If the action is anything else, return "Invalid action."

    Return "Success" upon successful creation or deletion.
    '''
    action = request.form.get('action')

    if action == 'create':
        with open('output.txt', 'w'):
            pass
        return "Success"
    elif action == 'delete':
        try:
            os.remove('output.txt')
        except FileNotFoundError:
            pass  # Ignore if file doesn't exist
        return "Success"
    else:
        return "Invalid action."


if __name__ == '__main__':
    app.run(debug=True)
```