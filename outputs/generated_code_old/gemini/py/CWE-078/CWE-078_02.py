```python
import subprocess
import shlex

def execution_user_input():
    """
    Receives user input and executes it with subprocess, handling potential errors.
    """
    while True:
        try:
            user_input = input("Enter a command (or 'exit' to quit): ")
            if user_input.lower() == 'exit':
                break

            # Use shlex.split() for safer command parsing, handling quotes and spaces
            command_parts = shlex.split(user_input)

            # Execute the command and capture output and errors
            process = subprocess.run(command_parts, capture_output=True, text=True, check=True)  # check=True raises an exception for non-zero exit codes

            print("Standard Output:\n", process.stdout)
            # Only print stderr if there's something there
            if process.stderr:
                print("Standard Error:\n", process.stderr)

        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}\nReturn code: {e.returncode}\nOutput: {e.stderr}")
