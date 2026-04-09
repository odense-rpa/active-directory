from ldap3 import Server, Connection

class ActiveDirectoryClient:
    
    def __init__(
        self,
        server_url: str,
        port: int,
        base_dn: str,
        username: str,
        password: str,         
    ) -> None:
       
        self.server = Server(server_url, port=port)
        self.connection = Connection(self.server, user=username, password=password, auto_bind=True)
        self.base_dn = base_dn
        self.search_filter = f"(sAMAccountName={username.split('@')[0]})"
        
    def søg(self, attributes: list):
        self.connection.search(self.base_dn, self.search_filter, attributes=attributes)
        return self.connection.entries
