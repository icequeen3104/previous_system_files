def authenticate_user(username, password):
    # Basic authentication logic
    if username == "admin" and password == "admin123":
        return True
    return False


def main():
    print("Application started")


if __name__ == "__main__":
    main()