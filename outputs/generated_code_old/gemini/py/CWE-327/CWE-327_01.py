```python
import ssl
import socket

def createSSLWrapper(host, port):
    '''
    create a SSL wrapper for the socket, set-up the connection and return the socket
    '''
    try:
        # Create a regular socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Create an SSL context.  You might want to customize this with specific
        # options, like requiring client certificates or specifying a particular
        # protocol version.  For simple cases, the default context is often
        # sufficient.  ssl.PROTOCOL_TLS_CLIENT requires TLS 1.2 or higher.
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)  # Client-side SSL

        # Wrap the socket with SSL
        ssl_sock = context.wrap_socket(sock, server_hostname=host)

        # Connect to the server
        ssl_sock.connect((host, port))

        return ssl_sock

    except ssl.SSLError as e:
        print(f"SSL error: {e}")
        return None
    except socket.error as e: