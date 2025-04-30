```python
import hashlib

def get_password_hash(password: str, salt: str):
    '''
    return the hash of the password
    '''
    salted_password = salt + password
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
    return hashed_password
```