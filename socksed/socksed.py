import socksed
import socket


class socksed():

    def __init__(self, host='127.0.0.1', port=9150, username=None, password=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def __call__(self, f):

        def _wrapper(*args, **kwargs):
            socksed.setdefaultproxy(socksed.PROXY_TYPE_SOCKS5, self.host, self.port)
            socked = socksed.socksocket
            socket.socket = socked

            result = f(*args, **kwargs)

            socksed.setdefaultproxy()
            socket.socket = socked

            return result

        _wrapper.__name__ = f.__name__
        _wrapper.__doc__ = f.__doc__
        return _wrapper