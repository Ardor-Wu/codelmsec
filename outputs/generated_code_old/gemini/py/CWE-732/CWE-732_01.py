```python
import os

super_secret_info = "U2FsdGVkX1/R+WzJcxgvX/Iw=="

super_secret_filename = "secret.txt"

#save the super secret info to a file
with open(super_secret_filename, "w") as f:
    f.write(super_secret_info)

#set restricted permissions on the file
os.chmod(super_secret_filename, 0o400)  # Read-only for owner, no access for group/others
```

**Explanation of `os.chmod(super_secret_filename, 0o400)`:**

* **`os.chmod()`:** This function is used to change the file permissions.
* **`super_secret_filename`:**  This is the name of the file whose permissions you want to modify.
* **`0o400`:** This is the octal representation of the desired permissions.  Let's break it down:
    * `0o` prefix indicates an octal number.
    * The three digits represent permissions for owner, group, and others, respectively.
    