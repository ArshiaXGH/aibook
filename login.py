def login():
    """Simple login function"""
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Simple hardcoded credentials (for demo purposes)
    valid_username = "admin"
    valid_password = "password123"
    
    if username == valid_username and password == valid_password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password")
        return False


if __name__ == "__main__":
    login()