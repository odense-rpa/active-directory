import os
from functionality.client import ActiveDirectoryClient

def test_active_directory_search():
    # Initialize the client with test parameters
    client = ActiveDirectoryClient(
        server_url=str(os.getenv("SERVER_URL")),
        port=int(str(os.getenv("SERVER_PORT"))),
        base_dn=str(os.getenv("BASE_DN")),
        username=str(os.getenv("USERNAME")),
        password=str(os.getenv("PASSWORD"))
    )
    
    # Perform a search operation
    search_base = str(os.getenv("BASE_DN"))
    search_filter = "(sAMAccountName=simof)"
    attributes = ['displayName', 'mail', 'odkLeder']
    
    results = client.search(search_base, search_filter, attributes)
    
    # Assert that results are returned (this is a placeholder assertion)
    assert results is not None