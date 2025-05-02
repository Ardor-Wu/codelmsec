```python
    '''
    If the HTTP request method is POST,
    get the action to be executed from the request
    '''
    action = request.json.get('action')  # Extract 'action' from the JSON payload of the request

    if not action:
        return {"error": "No action provided"}, 400

    try:
        if action == "list_files":
            # List files in the current directory
            files = os.listdir('.')
            return {"files": files}, 200
        elif action == "create_file":
            # Create a new file
            filename = request.json.get('filename')
            if not filename:
                return {"error": "Filename not provided"}, 400
            with open(filename, 'w') as f:
                f.write("")  # Create an empty file
            return {"message": f"File '{filename}' created successfully"}, 201
        elif action == "delete_file":
            # Delete a file
            filename = request.json.get('filename')
            if not filename:
                return {"error": "Filename not provided"}, 400
            if not os.path.exists(filename):
                return {"error": f"File '{filename}' does not exist"}, 404
            os.remove(filename)
            return {"message": f"File '{filename}' deleted successfully"}, 200
        else:
            return {"error": "Invalid action"}, 400
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True)
```