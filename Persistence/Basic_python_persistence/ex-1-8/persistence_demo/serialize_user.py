from persistence_demo.user import User

def save_user():
    user = User("john_doe", "john@example.com", "supersecret")
    json_string = user.to_json()
    print("Serialized User (excluding password):\n", json_string)

if __name__ == "__main__":
    save_user()
