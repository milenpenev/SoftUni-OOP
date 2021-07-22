class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        if 5 > len(username) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")

profile_with_invalid_username = Profile('Too_long_usernameeee', 'Any')