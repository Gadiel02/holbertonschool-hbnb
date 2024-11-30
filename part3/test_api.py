from app.models.user import User

def test_user_creation():
    user_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com"
    }
    user = User(**user_data)

    assert all([
        user.first_name == user_data["first_name"],
        user.last_name == user_data["last_name"],
        user.email == user_data["email"],
        user.is_admin is False  # Default value
    ])
    print("User creation test passed!")

if __name__ == "__main__":
    test_user_creation()
