"""
Explanation:
User class: Handles user data (name and email). It has a single responsibility of representing a user.
EmailService class: Handles sending emails. It has a single responsibility of managing email communication.
UserRegistration class: Handles user registration. It has a single responsibility of registering users and 
coordinating between the User and EmailService classes.
This design ensures that each class has a single reason to change, adhering to the SRP.


"""

# Class responsible for handling user data
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# Class responsible for sending emails
class EmailService:
    def send_email(self, email, subject, body):
        print(f"Sending email to {email}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")

# Class responsible for user registration
class UserRegistration:
    def __init__(self, email_service):
        self.email_service = email_service

    def register_user(self, name, email):
        user = User(name, email)
        self.email_service.send_email(
            user.email,
            "Welcome!",
            f"Hello {user.name}, thank you for registering!"
        )
        print(f"User {user.name} registered successfully.")


def main():
    """Create service objects and register example users."""
    email_service = EmailService()
    registration = UserRegistration(email_service)

    # Create/register a few users
    registration.register_user("Alice", "alice@example.com")
    registration.register_user("Bob", "bob@example.com")


if __name__ == "__main__":
    main()

