```python
from ctypes import CDLL, c_int, c_char_p, POINTER, Structure, cast, byref, create_string_buffer
from ctypes.util import find_library

class PamHandle(Structure):
    """Opaque handle as defined in pam_appl.h"""
    _fields_ = []

class PamMessage(Structure):
    """Single PAM message structure"""
    _fields_ = [
        ("msg_style", c_int),
        ("msg", c_char_p),
    ]

class PamResponse(Structure):
    """Single PAM response structure"""
    _fields_ = [
        ("resp", c_char_p),
        ("resp_retcode", c_int),
    ]

libpam = CDLL(find_library("pam"))

pam_start = libpam.pam_start
pam_start.restype = c_int
pam_start.argtypes = [c_char_p, c_char_p, POINTER(c_void_p), POINTER(PamHandle)]

pam_authenticate = libpam.pam_authenticate
pam_authenticate.restype