from dataclasses import dataclass
from tls_tunnel.constants import Client


@dataclass
class TunnelOptions:
    host: str
    port: int

    # auth options
    auth_login: str = None
    auth_password: str = None

    # headers options
    client: str = Client.CHROME
    secure: bool = False
    http2: bool = False
    server_name: str = None


@dataclass
class ProxyOptions:
    host: str
    port: int

    # auth_options
    auth_login: str = None
    auth_password: str = None