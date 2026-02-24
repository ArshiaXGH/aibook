def login(username, password):
    """Simple login function that validates credentials."""
    valid_users = {
        "admin": "password123",
        "user": "user456"
    }
    
    if username in valid_users and valid_users[username] == password:
        return True
    return False


def main():
    print("=== Simple Login System ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if login(username, password):
        print("✓ Login successful!")
    else:
        print("✗ Invalid credentials. Try again.")


if __name__ == "__main__":
    main()