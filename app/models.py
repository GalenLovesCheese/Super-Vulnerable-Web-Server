#Mock Database

# Mock user database 
users = [
    {"id": 1, "username": "David", "password": "pass1", "role": "user"},
    {"id": 2, "username": "Simon", "password": "pass2", "role": "user"},
    {"id": 3, "username": "admin", "password": "adminpass", "role": "admin"},
]

# Mock file database
files = {

    # Demo files assigned to David
    1: {"file_id": "123.pdf", "owner_id": 1, "description": "File 123 owned by David"},
    2: {"file_id": "124.pdf", "owner_id": 1, "description": "File 124 owned by David"},
    3: {"file_id": "125.pdf", "owner_id": 1, "description": "File 125 owned by David"},
    4: {"file_id": "126.pdf", "owner_id": 1, "description": "File 126 owned by David"},
    5: {"file_id": "127.pdf", "owner_id": 1, "description": "File 127 owned by David"},
    # Demo files assigned to Simon
    6: {"file_id": "456.pdf", "owner_id": 2, "description": "File 456 owned by Simon"},
    7: {"file_id": "457.pdf", "owner_id": 2, "description": "File 457 owned by Simon"},
    8: {"file_id": "458.pdf", "owner_id": 2, "description": "File 458 owned by Simon"},
    9: {"file_id": "459.pdf", "owner_id": 2, "description": "File 459 owned by Simon"},
    10: {"file_id": "460.pdf", "owner_id": 2, "description": "File 460 owned by Simon"},
    # Demo files assigned to Admin
    11: {"file_id": "789.pdf", "owner_id": 3, "description": "File 789 owned by Admin"},
    12: {"file_id": "790.pdf", "owner_id": 3, "description": "File 790 owned by Admin"},
    13: {"file_id": "791.pdf", "owner_id": 3, "description": "File 791 owned by Admin"},
    14: {"file_id": "792.pdf", "owner_id": 3, "description": "File 792 owned by Admin"},
    15: {"file_id": "793.pdf", "owner_id": 3, "description": "File 793 owned by Admin"}

}