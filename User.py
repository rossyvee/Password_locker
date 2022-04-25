import string


class User:
    """
    Class creates new instance of user class
    """

    list_of_users: list = []

    username: string
    password: string

    def __init__(self, username, password):
        self.password = password
        self.username = username

    def create_user(self):
        """
        Save a new user to the application
        """
        User.list_of_users.append(self)

    def delete_user(self):
        """
        Deletes user from list
        """

        User.list_of_users.remove(self)

    def __str__(self):
        return f"My name is {self.username} and my password is {self.password}"

    def new_credentials(self):
        """
        returns new user credentials
        """
        return {
            "username": self.username,
            "password": self.password
        }

    def find_by_username(self, username):
        """
        find user by username
        """

        for user in self.list_of_users:
            if user.username == username:
                return user


rose = User("roseline", "1234")

print(rose.new_credentials().get("password"))
