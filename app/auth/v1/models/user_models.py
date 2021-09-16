class UserModels:
    """
    Class for the user operations
    """

    users = []

    def __init__(self, username, email, password, confirm_password):
        """
        Initialize the user models
        """
        self.id = len(UserModels.users) + 1
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def save_user(self):
        """
        Method to register user instance and update the data structure
        """
        user_record = dict(
            id=self.id,
            username=self.username,
            email=self.email,
            password=self.password,
            confirm_password=self.confirm_password,
        )
        self.users.append(user_record)
