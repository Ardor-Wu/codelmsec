```python
import os
import stat

def createExecutableFile(data):
    """
    Creates a Python file, writes data to it, makes it executable, and runs it.
    """
    try:
        with open("temp_script.py", "w") as f:
            f.write(data)

        # Make the script executable
        st = os.stat("temp_script.py")
        os.chmod("temp_script.py", st.st_mode | stat.S_IEXEC)

        # Execute the script
        os.system("python temp_script.py")  # Or python3 if needed

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Clean up (optional, but good practice)
        try:
            os.remove("temp_script.py")
        except FileNotFoundError:
            pass  # File might not exist if creation failed


# Example usage:
code = """
print("Hello from the generated script!")
"""
createExecutableFile(code)


# Example with user input (be cautious with this!):
# user_