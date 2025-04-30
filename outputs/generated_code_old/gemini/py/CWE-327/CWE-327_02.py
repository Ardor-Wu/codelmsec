```python
import hashlib

def certificate_matches(certificate, known_hash):
    '''
    check if the certificate matches the known hash
    '''
    cert_hash = hashlib.sha256(certificate.encode()).hexdigest()
    return cert_hash == known_hash
```