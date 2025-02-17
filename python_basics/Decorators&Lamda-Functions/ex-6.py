def role_required(role):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role != role:
                print("Access Denied!")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator

@role_required("admin")
def delete_user(user_id):
    print(f"User {user_id} deleted!")

delete_user("admin", 42)
delete_user("guest", 42)